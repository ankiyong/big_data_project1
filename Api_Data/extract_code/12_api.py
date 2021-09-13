import requests
from bs4 import BeautifulSoup
import json
import csv

# 크롤링 해서 구 이름을 가져오자
def get_loc_name():
    loc_name = []
    url = 'https://www.seoul.go.kr/seoul/autonomy.do'
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    box = soup.find('div',{'class':'call-list'}).find_all('li',{'class':'tabcont'})
    for item in box:
        loc_name.append(item.find('strong').text)
    return loc_name



def get_info(loc_name):
    official_price = []
    year = [2017,2018,2019]
    key = '4174677349706f70373455597a785a'
    for loc in loc_name:
        for y in year:
            url = f'http://openapi.seoul.go.kr:8088/{key}/json/IndividuallyPostedLandPriceService/1/5/{loc}/ / / / /{y}'
            res = requests.get(url)
            data= res.json()['IndividuallyPostedLandPriceService']['row']
            official_price.append(data)
    return official_price


def final(price_info):
    loc_name = price_info['SIGUNGU_NM']
    price = price_info['JIGA']
    year = price_info['YEAR']
    return {
        'year': year,
        'location':loc_name,
        'price':price

    }

def get_final_info(official_price):
    final_info = []
    for price_info in official_price:
        for price_info1 in price_info:
            price = final(price_info1)
            final_info.append(price)
    return final_info

def save_to_file(final_info):
  file = open("../file/official_price.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(['기간','지역구','지가'])
  for info in final_info:
    writer.writerow(list(info.values()))
  return


loc = get_loc_name()
final_price = get_info(loc)
final_info = get_final_info(final_price)
save_to_file(final_info)





