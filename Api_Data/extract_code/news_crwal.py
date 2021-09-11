import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def bring_page():
    options = Options()
    options.binary_location= 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    driver = webdriver.Chrome("Driver/chromedriver",chrome_options = options)
    driver.get("https://search.naver.com/search.naver?where=news&query=%EC%B9%98%EC%95%88&nso=so%3Ar%2Cp%3Afrom20190101to20210911")
    return driver

def find_url(driver):
    url = []
    whole_page = driver.page_source
    soup = BeautifulSoup(whole_page,'html.parser')
    news_box = soup.find_all('div',{'class':'news_area'})
    for item in news_box:
        url.append(item.find('a')['data-url'])
    return url

def bring_all_url():
    urls = []
    driver = bring_page()
    for _ in range(1):
        urls.append(find_url(driver))
        driver.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div/a[2]').click()
        time.sleep(5)
    return urls
print(bring_all_url())


# 1년 단위로 가능