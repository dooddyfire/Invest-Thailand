import datetime
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#Fix
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
import schedule
#Insert file name

def scrape_invest():
    url = "https://th.investing.com/indices/major-indices"



    #Get bot selenium make sure you can access google chrome
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)

    soup = BeautifulSoup(driver.page_source,'html.parser')

    row = [i for i in soup.find_all('tr')]
    td_all_row = []
    for i in row: 
        td_all = [ d.text for d in i.find_all('td')][1:]
        td_all_row.append(td_all)
        print(td_all)

    result_data_lis = td_all_row[1:44]
    print(result_data_lis)

    json_dict = {}
    for j in result_data_lis: 
        json_dict[j[0]] = {'latest':j[1],'max':j[2],'min':j[3],'change':j[4],"percent change":j[5],"time":j[6] }

    print()
    print(json_dict)
    print()
    json_object = json.dumps(json_dict, indent = 4) 
    print(json_object)

    with open("investing.json", "w") as outfile:
        outfile.write(json_object)

    print()
    print("All done!")

schedule.every(10).seconds.do(scrape_invest)

# ดึงทุกวันตามเวลาที่กำหนด
#schedule.every().day.at("10:30").do(scrape_invest)

while True:
    schedule.run_pending()
    time.sleep(1)