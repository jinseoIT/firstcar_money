import pymongo
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)
dbId = os.getenv('DB_ADMIN_ID')
dbPw = os.getenv('DB_ADMIN_PW')

client = MongoClient('mongodb+srv://'+dbId+':'+dbPw+'@firstcar-money.ojfbk.mongodb.net/firstcar-money?retryWrites=true&w'
                     '=majority')
db = client.dbfirtcar


# DB에 저장할 차량 url을 가져옵니다.
def get_urls():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    #data = requests.get('https://auto.naver.com/car/mainList.nhn?page=1', headers=headers)
    data = requests.get('https://auto.naver.com/car/mainList.nhn?mnfcoNo=0&modelType=OS&order=1&importYn=N&lnchYY=-1&saleType=-1&page=7', headers=headers)

    soup = BeautifulSoup(data.content.decode('utf-8', 'replace'), 'html.parser')
    trs = soup.select('.model_group_new > .model_lst > li')
    #print(trs)
    for tr in trs:
        # 차량 이름
        car_name = tr.select_one('.model_name > .box > strong').text
        # 차량 이미지
        car_img = tr.select_one('.thmb > a > img')['src']
        # 차량 로고
        car_maker_img = tr.select_one('.emblem > img')['src']
        # 차량 타입
        car_type = tr.select_one('.lst > .info > a > span').text
        # 차량 연비
        car_fuel_effi  = tr.select_one('.lst > .mileage > .dt > .ell > .en').text
        # 차량 연료
        car_fuel = tr.select_one('.lst > .mileage > span:nth-child(4) > .ell').text
        # 차량 가격 - full
        car_price_full = tr.select_one('.lst > .price ').text
        # 차량 가격 - basic
        car_price = tr.select_one('.lst > .price ').text
        st = car_price.replace("출시", "").replace("만원", "")
        arr= []
        if st!= '가격정보없음':
            arr = st.strip().split("~")
            car_price = arr[0]
        else :
            car_price = 0

        print("=======================================")
        print(car_name)
        print(car_img)
        print(car_maker_img)
        print(car_type)
        print(car_fuel_effi)
        print(car_fuel)
        print(car_price_full)
        print(car_price)

def insert_carInfo(url, pageNum):

    strPage = str(pageNum)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    # data = requests.get('https://auto.naver.com/car/mainList.nhn?page=1', headers=headers)
    data = requests.get(url+'&page='+strPage, headers=headers)

    soup = BeautifulSoup(data.content.decode('utf-8', 'replace'), 'html.parser')
    trs = soup.select('.model_group_new > .model_lst > li')
    for tr in trs:
        # 차량 이름
        car_name = tr.select_one('.model_name > .box > strong').text
        # 차량 이미지
        car_img = tr.select_one('.thmb > a > img')['src']
        # 차량 로고
        car_maker_img = tr.select_one('.emblem > img')['src']
        # 차량 타입
        car_type = tr.select_one('.lst > .info > a > span').text
        # 차량 연비S
        car_fuel_efficiency = tr.select_one('.lst > .mileage > .dt > .ell > .en').text
        # 차량 연료
        car_fuel = tr.select_one('.lst > .mileage > span:nth-child(4) > .ell').text.strip()
        # 차량 가격 - full
        car_price_full = tr.select_one('.lst > .price ').text.replace("출시","").strip()
        # 차량 가격 - basic
        car_price = tr.select_one('.lst > .price ').text
        st = car_price.replace("출시", "").replace("만원", "")
        arr = []
        if st != '가격정보없음':
            arr = st.strip().split("~")
            car_price = arr[0]
        else:
            car_price = 0

        doc = {
            'car_name': car_name,
            'car_img': car_img,
            'car_maker_img': car_maker_img,
            'car_type': car_type,
            'car_fuel': car_fuel,
            'car_fuel_efficiency': car_fuel_efficiency,
            'car_price_full': car_price_full,
            'car_price': car_price
        }
        db.carInfo.insert_one(doc)
        print('완료!!', car_name)

def insert_cars():
    # 시판모델 최신 출시일 desc url
    newModelUrl = "https://auto.naver.com/car/mainList.nhn?mnfcoNo=0&modelType=OS&order=1&importYn=N&lnchYY=-1&saleType=-1"
    newModelPageCnt = 7
    # 단종모델 최신 출시일 desc url
    oldModelUrl = "https://auto.naver.com/car/mainList.nhn?mnfcoNo=0&modelType=DC&order=1&importYn=N"
    oldModelPageCnt = 35

    #db reset
    db.carInfo.drop()
    # 단종모델 insert
    for i in range(1, oldModelPageCnt + 1):
        insert_carInfo(oldModelUrl, i)

    # 시판모델 insert
    for i in range(1, newModelPageCnt+1):
        insert_carInfo(newModelUrl, i)



## 실행하기
insert_cars()