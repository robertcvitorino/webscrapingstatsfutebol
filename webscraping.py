from os import name
import time
from pandas.core.indexing import IndexSlice
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from tabulate import tabulate
import json

paises = {
        'leaguebrazil': {'field': 'brazil' },
        'leaguebrazil2': {'field': 'brazil2'},        
        'leagueargentina': {'field': 'argentina' },
        'leagueaustria': {'field': 'austria'},
        'leagueaustralia': {'field': 'australia'},
        'leaguebelgium': {'field': 'belgium'},
        'leaguegermany': {'field': 'germany'},
        'leaguegermany2': {'field': 'germany2'},
        'leaguedenmark': {'field': 'denmark'},
        'leagueengland': {'field': 'england'},
        'leagueengland2': {'field': 'england2'},
        'leaguespain': {'field': 'spain'},
        'leaguespain2': {'field': 'spain2'},
        'leaguefinland': {'field': 'finland'},
        'leaguefrance': {'field': 'france'},
        'leaguefrance2': {'field': 'france2'},
        'leaguenetherlands': {'field': 'netherlands'},
        'leagueitaly': {'field': 'italy'},
        'leagueitaly2': {'field': 'italy2'},
        'leaguejapan': {'field': 'japan'},
        'leaguenorway': {'field': 'norway'},
        'leaguepoland': {'field': 'poland'},
        'leagueportugal': {'field': 'portugal'},
        'leaguerussia': {'field': 'russia'},
        'leaguescotland': {'field': 'scotland'},
        'leaguesweden': {'field': 'sweden'},
        'leagueturkey': {'field': 'turkey'},
    }
def acessosite(type):   
    try:

    
        field=paises[type]['field']
     
        url = f"https://www.soccerstats.com/trends.asp?league={field}"
        # Pega link do site da NBA e abre o navegador Firefox
        option =Options()
        option.headless=True
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get(url)
        #Aceito os termos de cookies do site
        acept_cookies=WebDriverWait(driver,5).until(
            EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/button[3]"))).click()
        time.sleep(10)    
        #navega na tabela e clica no filtro do + 1.5
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div[5]/div[2]/table[1]/tbody/tr/td/table[1]/thead/tr/th[5]").click()  
        #pega todo os dados da tabela
        element = driver.find_element_by_xpath("//*[@id='btable']")
        #Convert os dado html
        html_content = element.get_attribute('outerHTML') 
        
        #Parsear os dados doa html 
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find(name='table')   
        #Busca somente o cabecario da tabela 
        df_full = pd.read_html(str(table),header=1)[0].head(20)        
        #define o cabeçario da tabela
        df_full.columns = ['Matches of','GP','Avg','0.5+','1.5+','2.5+','3.5+','4.5+','5.5+','BTS','CS','FTS', 'WTN','LTN']  
        
    finally:    
        driver.quit()
    return df_full
    
path_excel=f"C:/Users/Robert/Documents/Programação/Workspace/webscrapingstatsfutebol/webscrapingstatsfutebol/databases/futebol.xlsx"
writer = pd.ExcelWriter(path_excel, engine='xlsxwriter')
for k in paises:
    df=acessosite(k)       
    df.to_excel(writer, sheet_name=f'{k}')

writer.save()

        #print(f"INDEX 0 da pagina \n\n{df_full}")   
        
        #Path onde salva o Excel
    
        #Salvando o excel
        #pd.DataFrame.to_excel(df_full,path_excel,sheet_name='Brasileirao')
        #df_full.to_excel(path_excel,sheet_name='Brasileirao')

   
    




















#WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='onetrust-accept-btn-handler']"))).click()
    #element = driver.find_element_by_xpath("//*[@class='event__match event__match--oneLine']")   
    #element = driver.find_element_by_xpath("//*[@id='g_1_KSc2Iwq3']")       
    #driver.find_element_by_xpath("/html/body/div[1]/main/div/div[2]/div/div[3]/div[2]/div/div/div/div/div[6]").click()    
    #time.sleep(10) 
    #driver.find_element_by_css_selector(".styles__InnerWrapper-sc-133iacn-2 > div:nth-child(1) > a:nth-child(3)").click()
    #time.sleep(10) 
    #driver.find_element_by_xpath("//*[@id='btable']").click()

#/html/body/div[1]/main/div/div[2]/div/div[5]/div/div[1]/div/div[2]/div[1]/div/div/a[3]
#html body div#__next main div.Container-sc-119xkyt-0.hZaeKU div.Content__PageContainer-sc-14479gi-0.styles__ListPageContent-sc-1wq2t22-3.jFsElm div.Grid-sc-1kxv72p-0.gVSUkA div.Col-pm5mcz-0.styles__SidebarCol-sc-1wq2t22-0.eCYZUh div.styles__Wrapper-sc-1c9nn5b-0.HoJZc.ps.ps--active-y div div.styles__StyledWidget-d389b-3.lkbfzE.widget div.TabsWrapper__Wrapper-sc-5ag92o-0.iFonsX div.styles__Wrapper-sc-133iacn-1.fbebFr div.styles__InnerWrapper-sc-133iacn-2.izpTpz div.Tabs__Header-vifb7j-0.bpUSvK a.Label-sc-19k9vkh-0.bfqsCw
#Label-sc-19k9vkh-0:nth-child(3)  