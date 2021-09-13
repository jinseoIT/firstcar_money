import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.firstCar_money


# DB에 저장할 차량 url을 가져옵니다.
def get_urls():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://auto.danawa.com/newcar', headers=headers)

    soup = BeautifulSoup(data.content.decode('utf-8', 'replace'), 'html.parser')

    trs = soup.select('.model_lst  > li')

    for tr in trs:
        #print(tr)
        name = tr.select_one('.model_ct > .model_name').text
        print(name)

#def insert_carInf(url):


## 실행하기
get_urls()