
# coding: utf-8

# In[26]:

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

"""example url for stock no. 0050
http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/genpage/Report201509/
201509_F3_1_8_0050.php?STK_NO=0051&myear=2015&mmon=09
"""

#url = 'http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/genpage/Report201509/201509_F3_1_8_0051.php'

year = '2015'
month = '09'
stock_num = '0050'
y_month = year + month


base_url = 'http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/genpage/'
para1 = 'Report{y_month}/{y_month}_F3_1_8_{stock_num}.php'.format(y_month=y_month, stock_num=stock_num)
para2 = '?STK_NO={stock_num}&myear={year}&mmon={month}'.format(stock_num=stock_num, year=year, month=month)

url = base_url + para1 + para2

#print url

dcap = dict(DesiredCapabilities.PHANTOMJS)

# set user agent
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87"
)

# use phantomJS as client for some javascript in html
browser = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--load-images=no'])
#browser = webdriver.PhantomJS(desired_capabilities=dcap)

browser.get(url)

#print browser.page_source

soup = BeautifulSoup(browser.page_source, "html.parser")

# get the price
for item in soup.findAll('tbody'):
    for i in item.findAll('td', {'align': 'right'}):
        print i.text

