import requests
from bs4 import BeautifulSoup
import json
import csv


def access_api():
    url = 'https://api.odcloud.kr/api/15076962/v1/uddi:8ba698ca-b192-4fb7-99f7-e60903af03d0?page=1&perPage=165&serviceKey=rEGaAvc%2FhtgpEP4%2B%2B7dS7BUBhfbPxPmh6VXlLp4gMULjsBx30IjRvCENmSw0svqwc6V%2BXDsMvW86rxMViO8cMQ%3D%3D'
    res = requests.get(url)
    return res

def whole_data(res):
    data = res.json()
    info_box = data['data']
    return info_box

def extract_info(info):
    office = info['경찰서']+'경찰서'
    loc = info['주소']
    chi = info['치안센터명']
    return {"경찰서":office,
            "주소":loc,
            "치안센터명":chi}

def final_(info_box):
    final_info = []
    for info in info_box:
        final_info.append(extract_info(info))
    return final_info



def save_to_file(final_info):
  file = open("../file/loc_police.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(['경찰서','주소','치안센터명'])
  for info in final_info:
    writer.writerow(list(info.values()))
  return

res = access_api()
info_box = whole_data(res)
final_info = final_(info_box)
save_to_file(final_info)