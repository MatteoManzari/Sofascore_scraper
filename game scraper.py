from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import csv

#it/newcastle-united-tottenham-hotspur/IO
def find_str(s, char):
    index = 0
    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index
            index += 1
    return -1

def removesign(text,bro):
    if bro=='-':
        text=0
        return(text)
    else:
        text=bro
        return(text)


#csv_file = 'C:\\Users\\Matteo\\Desktop\\Statistical Learning project\\Blocco-partite-premier-league-2016-17.txt'
csv_file='...'
results = []
with open(csv_file, newline='') as inputfile:
    for row in csv.reader(inputfile):
        for el in row:
            results.append(el.strip())


Big_dict={}
BD={}
shits1=[]
for _url in results:
    try:
        shits= []
        url='https://www.sofascore.com'+_url
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(executable_path="C:/Users/Matteo/Downloads/chromedriver",chrome_options=chrome_options)
    
        driver.get(url)
        try:
            
            driver.find_element_by_link_text('Statistiche giocatore').click()            
            
            #riepilogo
            driver.find_element_by_link_text('Riepilogo').click()    
            soup = BeautifulSoup(driver.page_source, "lxml")
            
            
            TITLE=soup.find_all('h2')[0].get_text().replace('\n','')
            squads=TITLE.split('-')
            rpc=soup.find_all('div', class_="cell__content u-pT8")[0].get_text().replace('\n','').strip().replace(' ','')#.split('-')
            
            if '1'>'2':
                squads[0]
            elif '1'=='2':
                'X'
            else:
                squads[0]
            
            
            soup = BeautifulSoup(str(soup)[find_str(str(soup),'id="player-statistics-tab-summary">'):], "lxml")
            

            Total_dict= {}
            secondary_dict={}

            #summary table
            table=soup.find('table',"table table--statistics js-sorter-body sort-by-rating")
            headings = [th.get_text() for th in table.find("tr").find_all("th")][1::]
            datasets_riepilogo = []
            dataset=[]
            for row in table.find_all("tr")[1:]:
                aux= list(td for td in row.find_all("td"))[0]
                team=[re.search('(?<=title=")(.*)', str(aux.contents[1])).group(0)[:-3]]
                dataset =list(td.get_text().strip() for td in row.find_all("td")) + team
                datasets_riepilogo.append(dataset)
            
            #Attacco
            driver.find_element_by_link_text('Attacco').click()    
            soup = BeautifulSoup(driver.page_source, "lxml")
            soup = BeautifulSoup(str(soup)[find_str(str(soup),'id="player-statistics-tab-attack">'):], "lxml")
                      
            #summary table
            table_attacco=soup.find('table',"table table--statistics js-sorter-body sort-by-rating")
            headings = [th.get_text() for th in table_attacco.find("tr").find_all("th")][1::]
            datasets_attacco = []
            dataset=[]
            for row in table_attacco.find_all("tr")[1:]:
                aux= list(td for td in row.find_all("td"))[0]
                team=[re.search('(?<=title=")(.*)', str(aux.contents[1])).group(0)[:-3]]
                dataset =list(td.get_text().strip() for td in row.find_all("td")) + team
                datasets_attacco.append(dataset)
           
            ##Difesa
            driver.find_element_by_link_text('Difesa').click()    
            soup = BeautifulSoup(driver.page_source, "lxml")
            soup = BeautifulSoup(str(soup)[find_str(str(soup),'id="player-statistics-tab-defence"'):], "lxml")
            
            
            #summary table
            table_difesa=soup.find('table',"table table--statistics js-sorter-body sort-by-rating")
            headings = [th.get_text() for th in table_difesa.find("tr").find_all("th")][1::]
            datasets_difesa = []
            dataset=[]
            for row in table_difesa.find_all("tr")[1:]:
                aux= list(td for td in row.find_all("td"))[0]
                team=[re.search('(?<=title=")(.*)', str(aux.contents[1])).group(0)[:-3]]
                dataset =list(td.get_text().strip() for td in row.find_all("td")) + team
                datasets_difesa.append(dataset) 
            
            ###Passando
            driver.find_element_by_link_text('Passando').click()    
            soup = BeautifulSoup(driver.page_source, "lxml")
            soup = BeautifulSoup(str(soup)[find_str(str(soup),'id="player-statistics-tab-passing">'):], "lxml")
            
            #summary table
            table_passando=soup.find('table',"table table--statistics js-sorter-body sort-by-rating")
            headings = [th.get_text() for th in table_passando.find("tr").find_all("th")][1::]
            datasets_passando = []
            dataset=[]
            for row in table_passando.find_all("tr")[1:]:
                aux= list(td for td in row.find_all("td"))[0]
                team=[re.search('(?<=title=")(.*)', str(aux.contents[1])).group(0)[:-3]]
                dataset =list(td.get_text().strip() for td in row.find_all("td")) + team
                datasets_passando.append(dataset)
            
            ###Contrasti
            driver.find_element_by_link_text('Contrasti').click()    
            soup = BeautifulSoup(driver.page_source, "lxml")
            soup = BeautifulSoup(str(soup)[find_str(str(soup),'id="player-statistics-tab-duels">'):], "lxml")
            
            #summary table
            table_contrasti=soup.find('table',"table table--statistics js-sorter-body sort-by-rating")
            headings = [th.get_text() for th in table_contrasti.find("tr").find_all("th")][1::]
            datasets_contrasti = []
            dataset=[]
            for row in table_contrasti.find_all("tr")[1:]:
                aux= list(td for td in row.find_all("td"))[0]
                team=[re.search('(?<=title=")(.*)', str(aux.contents[1])).group(0)[:-3]]
                dataset =list(td.get_text().strip() for td in row.find_all("td")) + team
                datasets_contrasti.append(dataset)
            
            
            for q in range(len(datasets_riepilogo)):
                
                #changing dataset
                player=datasets_riepilogo[q]
                _id=player[1]
                Total_dict[_id]={}
                secondary_dict[_id]={}
                Total_dict[_id]['Partita']= TITLE
                Total_dict[_id]['Risultato']= rpc
                Total_dict[_id]['Numero_maglia']= player[0]
                Total_dict[_id]['Nome']= player[1]
                Total_dict[_id]['Gol']=0
                Total_dict[_id]['Gol']=removesign(Total_dict[_id]['Gol'],player[2])
                Total_dict[_id]['Assist']=0
                Total_dict[_id]['Assist']=removesign(Total_dict[_id]['Assist'],player[3])
                Total_dict[_id]['Contrasti']= player[4]
                Total_dict[_id]['Uno contro uno']=int(re.search("\d+",player[6]).group(0))
                if  Total_dict[_id]['Uno contro uno']==0:
                    Total_dict[_id]['Uno contro uno riusciti']=0
                else:    
                    Total_dict[_id]['Uno contro uno riusciti']=round(int(re.search("\(\d+\)",player[6]).group(0)[1:-1])/int(re.search("\d+",player[6]).group(0)),2)
                Total_dict[_id]['Minuti giocati']= player[7]
                Total_dict[_id]['Posizione']= player[8]
                Total_dict[_id]['Valutazione']= player[9]
                Total_dict[_id]['Squadra']= player[10]
                if rpc.split('-')[0]>rpc.split('-')[1]:
                    Total_dict[_id]['Match_winner']  = TITLE.split('-')[0]  
                elif rpc.split('-')[0]<rpc.split('-')[1]:
                    Total_dict[_id]['Match_winner']  = TITLE.split('-')[1]            
                else:
                    Total_dict[_id]['Match_winner']= 'Pareggio'


                #changing dataset
                player=datasets_attacco[q]
                _id=player[1]
                Total_dict[_id]['Tiri in porta']= player[2]
                Total_dict[_id]['Tiri fuori']= player[3]
                Total_dict[_id]['Tiri bloccati']= player[4]
                Total_dict[_id]['Dribbling tentati']= int(re.search("\d+", player[5]).group(0))
                if Total_dict[_id]['Dribbling tentati']==0:
                    Total_dict[_id]['Dribbling tentati riusciti'] =0
                else:
                    Total_dict[_id]['Dribbling tentati riusciti']=round(int(re.search("\(\d+\)", player[5]).group(0)[1:-1])/int(re.search("\d+",player[5]).group(0)),2)
                aux=player[6].replace('\n',':').split(': ')
                for i in range(len(aux)):
                    j=aux[i].strip()
                    if i%2!=0:
                        try:
                            secondary_dict[_id][aux[i-1].strip()]= int(re.match('\d+',j).group(0))
                        except:
                            secondary_dict[_id][aux[i-1].strip()]= int(j)
                    else:
                        shits.append(j)
                     
                        
                #changing dataset
                player=datasets_difesa[q]
                _id=player[1]
                Total_dict[_id]['Salvataggi']= player[2]
                Total_dict[_id]['Tiri bloccati']= player[3]
                Total_dict[_id]['Intercetti']= player[4]
                Total_dict[_id]['Dribbling_subiti']=0
                Total_dict[_id]['Dribbling_subiti']= removesign(Total_dict[_id]['Dribbling_subiti'],player[6])
                aux=player[7].replace('\n',':').split(':')
                for i in range(len(aux)):
                    j=aux[i].strip()
                    if i%2!=0:
                        try:
                            secondary_dict[_id][aux[i-1].strip()]= int(re.match('\d+',j).group(0))
                        except:
                            secondary_dict[_id][aux[i-1].strip()]= int(j)
                    else:
                        shits.append(aux[i].strip())
                
                
                #changing dataset 
                player= datasets_passando[q]
                _id=player[1]
                Total_dict[_id]['Passaggi effettuati']= re.search("\d+", player[2]).group(0)
                if re.search("\(\d+%\)",player[2]).group(0)[1:-2]!='100':
                    Total_dict[_id]['Precisione_passaggi']='0.'+re.search("\(\d+%\)",player[2]).group(0)[1:-2]
                else:
                    Total_dict[_id]['Precisione_passaggi']='1'
                Total_dict[_id]['Passaggi chiave']= player[3]
                Total_dict[_id]['Cross']= int(re.search("\d+",player[4]).group(0))
                if  Total_dict[_id]['Cross']==0:
                     Total_dict[_id]['Cross prec.']=0
                else:
                     Total_dict[_id]['Cross prec.']=round(int(re.search("\(\d+\)", player[4]).group(0)[1:-1])/int(re.search("\d+", player[4]).group(0)),2)           
                Total_dict[_id]['Palle lunghe']= int(re.search("\d+", player[5]).group(0))
                if  Total_dict[_id]['Palle lunghe']==0:
                     Total_dict[_id]['Palle lunghe riusciti']=0
                else:
                     Total_dict[_id]['Palle lunghe riusciti']=round(int(re.search("\(\d+\)", player[5]).group(0)[1:-1])/int(re.search("\d+", player[5]).group(0)),2)
                
                aux=player[6].replace('\n',':').split(':')
                for i in range(len(aux)):
                    j=aux[i].strip()
                    if i%2!=0:
                        try:
                            secondary_dict[_id][aux[i-1].strip()]= int(re.match('\d+',j).group(0))
                        except:
                            secondary_dict[_id][aux[i-1].strip()]= int(j)
                    else:
                        shits.append(aux[i])
                
                #changing dataset
                player=datasets_contrasti[q]
                Total_dict[_id]['Palle_perse']= player[3]
                Total_dict[_id]['Falli subiti']= player[4]
                Total_dict[_id]['Falli']= player[5]
                        
            ##portiere
            driver.find_element_by_link_text('Portiere').click()    
            soup = BeautifulSoup(driver.page_source, "lxml")
            soup = BeautifulSoup(str(soup)[find_str(str(soup),'"player-statistics-tab-goalkeeper"'):], "lxml")
            
            #summary table
            table_portiere=soup.find('table',"table table--statistics js-sorter-body sort-by-rating")
            headings = [th.get_text() for th in table_portiere.find("tr").find_all("th")][1::]
            datasets_portiere = []
            dataset=[]
            for row in table_portiere.find_all("tr")[1:]:
                aux= list(td for td in row.find_all("td"))[0]
                team=[re.search('(?<=title=")(.*)', str(aux.contents[1])).group(0)[:-3]]
                dataset =list(td.get_text().strip() for td in row.find_all("td")) + team
                datasets_portiere.append(dataset)
#            gk=[]
            dict_portiere={}
#            _id=0
            for player in datasets_portiere:
                _id=player[1]
                dict_portiere[_id]={}
                dict_portiere[_id]['Numero_maglia']= player[0]
                dict_portiere[_id]['Nome']= player[1]
                dict_portiere[_id]['Salvataggi']= player[2]
                dict_portiere[_id]['Respinte']= player[3]
    #            dict_portiere[_id]['Uscite (vincenti)']= player[4]
                dict_portiere[_id]['Uscite']= int(re.search("\d+",player[4]).group(0))
                if dict_portiere[_id]['Uscite']==0:
                    dict_portiere[_id]['Uscite Vincenti']=0
                else:
                    
                    dict_portiere[_id]['Uscite Vincenti']=round(int(re.search("\(\d+\)", player[4]).group(0)[1:-1])/int(re.search("\d+", player[4]).group(0)),2)
    
                dict_portiere[_id]['Duelli di testa vinti']= player[5]
                aux=player[6].replace('\n',':').split(':')  
                for i in range(len(aux)):
                    j=aux[i].strip()
#                    print(j)
                    if i%2!=0:
                        try:
                            dict_portiere[_id][aux[i-1].strip()]= int(re.match('(?<=\\\)\d+',j).group(0))
                        except:
                            dict_portiere[_id][aux[i-1].strip()]= int(j)
                    else:
                        shits.append(aux[i].strip())
#                        gk.append(aux[i].strip())
#                _id+=1
#            gk=list(set(gk))
            names_gk=[]
            for _id in dict_portiere.keys():
                names_gk.append(dict_portiere[_id]['Nome'])
            for _id in Total_dict.keys():
                   if Total_dict[_id]['Nome'] in names_gk:
                       mm= [key for key in dict_portiere.keys() if Total_dict[_id]['Nome'] == dict_portiere[key]['Nome'] ] 
                       for k in dict_portiere[mm[0]].keys():
                           Total_dict[_id][k]=dict_portiere[mm[0]][k]
        #                       Total_dict[_id][k]=0
                   else:
                        for k in list(dict_portiere[list(dict_portiere.keys())[0]].keys()):
                            if k not in Total_dict[_id].keys():
                                Total_dict[_id][k]=0
            shits= list(set(shits))
            shits.remove('-')
            print(shits)
            shits1+=shits
            Big_dict[_url]= Total_dict
            BD[_url]=secondary_dict
            print('fatto! '+ _url)
            driver.close()
        except Exception as exc:
           
            print (exc)
            print('ahia!!!! ' + _url)
            results.remove(_url)
            driver.close()
    except:
        print('no url!')
        


shits1=list(set(shits1))
count1=0
count2=0
for game in BD.keys():
    for play in BD[game].keys():
        for shitta in shits1:
            count1+=1
            if shitta not in list(BD[game][play].keys()):
                BD[game][play][shitta]=0
                count2+=1

for game in BD.keys():
    for play in BD[game].keys(): 
        for key in BD[game][play].keys():
            if key not in Big_dict[game][play].keys():
                Big_dict[game][play][key]=BD[game][play][key]        
                

###Save_ur_job
#csv_file = 'C:\\Users\\Matteo\\Desktop\\Statistical Learning project\\p1617.csv'
csv_file='...'
csv_columns = list(Big_dict[game][play].keys())
with open(csv_file, "w", encoding='utf-8') as f:  #UnicodeEncodeError: without utf-8
    writer = csv.writer(f)
    writer.writerow(csv_columns)
    for key1 in Big_dict.keys():
        for key in Big_dict[key1].keys():
            aux=[ Big_dict[key1][key][key2] for key2 in csv_columns ]
            writer.writerow(aux)
#debugging game links
#csv_file = 'C:\\Users\\Matteo\\Desktop\\Statistical Learning project\\deb_games.csv'
csv_file='...'
with open(csv_file, "w",) as f:  #UnicodeEncodeError: without utf-8
    writer = csv.writer(f)
    writer.writerow(results)

