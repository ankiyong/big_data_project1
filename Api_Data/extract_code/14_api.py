import requests
from bs4 import BeautifulSoup
import json
import csv

key = '4174677349706f70373455597a785a'
url = f'http://openapi.seoul.go.kr:8088/{key}/json/womanSafeAreaInfo/1/1000/'
res = requests.get(url)
data = res.json()['womanSafeAreaInfo']['row']


def final(info):
    location = info['GU_NM']
    addr = info['ADDR']
    return {
        'location':location,
        'address':addr
        }
def get_info(data):
    loc_info = []
    for info in data:
        infomation = final(info)
        loc_info.append(infomation)
    return loc_info


def save_to_file(loc_info):
  file = open("../file/loc_info.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(['location','address'])
  for info in loc_info:
    writer.writerow(list(info.values()))
  return

loc_info = get_info(data)
save_to_file(loc_info)
print(loc_info)