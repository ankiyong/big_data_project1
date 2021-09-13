import requests
from bs4 import BeautifulSoup
import json
import csv
# 1481
def access_api():
    p = 1
    page = 1481
    url = f'https://api.odcloud.kr/api/15054711/v1/uddi:f038d752-ff35-4a22-a2c2-cf9b90de7a30?page={p}&perPage={page}&serviceKey=rEGaAvc%2FhtgpEP4%2B%2B7dS7BUBhfbPxPmh6VXlLp4gMULjsBx30IjRvCENmSw0svqwc6V%2BXDsMvW86rxMViO8cMQ%3D%3D'
    res = requests.get(url)
    return res

def whole_data(res):
    data = res.json()
    info_box = data['data']
    return info_box

def extract_info(info):


    name = info['서']
    address = info['주소']
    pa = info['지구대파출소']
    return {


        "경찰서":name,
        "주소":address,
        "파출소":pa
    }

def final_(info_box):
    final_info = []
    for info in info_box:
        final_info.append(extract_info(info))
    return final_info[1207:]


def save_to_file(final_info):
  file = open("../file/loc_police_office.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(['경찰서','주소','파출소명'])
  for info in final_info:
    writer.writerow(list(info.values()))
  return


res = access_api()
info_box = whole_data(res)
final_info = final_(info_box)
save_to_file(final_info)