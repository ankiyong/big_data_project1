from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# webdriver 객체 생성
driver = webdriver.Chrome('C:\chromedriver\chromedriver')
# 지연
driver.implicitly_wait(3)
# 페이지 접근
url ='https://openab.seoul.go.kr/build/info.do?gubun=document'
driver.get(url)

# 개별 정보 가져오기
def get_product_info(text) :
    p_tag = text.find("a",{})
    td = text.findAll("td")

    return{"대장종류":td[0].text,"주용도":td[1].text,"건물위치":p_tag.text,"건물명":td[3],"연면적":td[4],"건축면적":td[5]}

# 페이지 정보 가져오기
def get_page_products(url) :
    url= url
    url ='https://openab.seoul.go.kr/build/info.do?gubun=document'

    # xpath 4~13 반복
    global i_num
    if i_num == 14 :
        i_num = 4

    # 코드 추출
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.find("tbody",{})
    prd_boxes= ul.findAll("tr")
    prod_info_list = [get_product_info(text) for text in prd_boxes]

    # 페이지 이동
    xpath = '//*[@id="contents"]/div[5]/ul/li['+ str(i_num) +']/a' # 버튼 xpath
    driver.find_element_by_xpath(xpath).click() # 클릭
    i_num += 1

    return prod_info_list

url ='https://openab.seoul.go.kr/build/info.do?gubun=document'
i_num = 4
df_fin = pd.DataFrame()

# 데이터프레임 생성
for i in range(1,61192) : # 가져올 페이지 수
    url ='https://openab.seoul.go.kr/build/info.do?gubun=document'
    page_product = get_page_products(url)
    df = pd.DataFrame(page_product)
    df_fin = pd.concat([df_fin,df],axis=0,ignore_index=True)

#print(df_fin)
#df_fin.to_csv('프젝_2_건물.csv', encoding = 'utf-8')
