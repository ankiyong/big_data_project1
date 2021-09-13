import requests
from bs4 import BeautifulSoup
import json
import csv
def access_api():
    url = f"https://api.odcloud.kr/api/15036460/v1/uddi:8b02c6c2-68f7-47da-a272-b43bf236595d?page=1&perPage=10&serviceKey=rEGaAvc%2FhtgpEP4%2B%2B7dS7BUBhfbPxPmh6VXlLp4gMULjsBx30IjRvCENmSw0svqwc6V%2BXDsMvW86rxMViO8cMQ%3D%3D"
    res = requests.get(url)
    return res

def whole_data(res):
    data = res.json()
    info_box = data['data']
    return info_box


def extract_info(info):
    seven_teen = info['2017년']
    eight_teen = info['2018년']
    nine_teen = info['2019년']
    loc = "서울"+info['경찰서']+"경찰서"
    return {
            "경찰서명": loc,
            "2017":seven_teen,
            "2018":eight_teen,
            "2019":nine_teen
            }


def final_(info_box):
    final_info = []
    for info in info_box:
       final_info.append(extract_info(info))
    return final_info

def save_to_file(final_info):
  file = open("../file/police_man.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(['경찰서명','2017','2018','2019'])
  for info in final_info:
    writer.writerow(list(info.values()))
  return


res = access_api()
info_box = whole_data(res)
final_info = final_(info_box)
save_to_file(final_info)
print(final_info)

