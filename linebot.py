from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


import requsts
import datetime


now = datetime.datetime.today()
today = now.strftime("%-m/%-d")
URL = 'https://g-sys.toyo.ac.jp/univision/www/html/kyukoC14.html'


options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',chrome_options=options)
driver.get(URL)

driver.find_element_by_id('form1:htmlUserId').send_keys("[ID]")
driver.find_element_by_id('form1:htmlPassword').send_keys("[PASSWORD]")
driver.find_element_by_id('form1:login').click()

number = soup.findAll('span', id="form1:Poa00201A:htmlParentTable:htmlDetailTbl2:htmlListCount")
info_count = int(number[0].contents[0].replace('件',""))
print('合計件数'+str(info_count))

out_data = ""
for number in range(info_count):
    info_data = soup.find('span', id="form1:Poa00201A:htmlParentTable:0:htmlDetailTbl2:"+ str(number) +":htmlTitleCol3")
    info_text = info_data.get_text()
    print(info_text)
    if info_text.find(str(today)) != -1:
        out_data = out_data + "\n" +info_data.get_text() 
if out_data == "":
    out_data = '\n本日、休講および補講はないはずです'
    print (out_data)
    
    
   send_data = {"value1": today ,"value2": out_data}
headers = {'Content-Type': "application/json"}
url = 'https://maker.ifttt.com/trigger/[イベント名]/with/key/[APIKEY]'
response = requests.post(url, json=send_data, headers=headers)
print (response.status_code)
driver.quit()
