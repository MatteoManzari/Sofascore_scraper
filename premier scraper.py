NOT WORKING :(


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv

url='https://www.sofascore.com/tournament/football/england/premier-league/17'

      
##We did it
years=['01/02','02/03','03/04','04/05','05/06','06/07','07/08','08/09','09/10','10/11','11/12','12/13','13/14','14/15','15/16','16/17','17/18']  

hrefs=[]

for year in years:
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path="C:/Users/Matteo/Downloads/chromedriver",chrome_options=chrome_options)

    driver.get(url)
    driver.find_element_by_class_name("dropdown__toggle--compact").click()  
    driver.find_element_by_link_text(year).click() 
    
    
    
    soup = BeautifulSoup(driver.page_source, "lxml")
    control=True
    while control:
        try:                
            fo=soup.find('div','js-event-list-tournament tournament')            
            for link in fo.find_all('a'):
                hrefs.append(link.get('href'))
            driver.find_element_by_class_name('js-tournament-page-show-previous-week').click() 
        except:
            control=False

    
        
    driver.close()    

#csv_file = 'C:\\Users\\Matteo\\Desktop\\Statistical Learning project\\hrefs.csv'
csv_file='...'
with open(csv_file, "w",) as f:  #UnicodeEncodeError: without utf-8
    writer = csv.writer(f)
    writer.writerow(hrefs)

