from flask import render_template, Blueprint, request, jsonify
from pymongo import MongoClient
import os

api_car = Blueprint('api_car', __name__, template_folder="templates")


dbId = os.getenv('DB_ADMIN_ID')
dbPw = os.getenv('DB_ADMIN_PW')

client = MongoClient(
    'mongodb+srv://' + dbId + ':' + dbPw + '@firstcar-money.ojfbk.mongodb.net/firstcar-money?retryWrites=true&w'
                                           '=majority')
db = client.dbfirtcar

# 차량 리스트 페이지
@api_car.route('/car/list')
def home():
    page = int(request.args.get('page', 1))
    limit = 16
    offset = (page - 1) * limit
    # default 출시순 desc
    car_list = list(db.carInfo.find({}, {'_id': False}).sort('car_age', -1).limit(limit).skip(offset))
    return render_template('carList.html', carList=car_list)

# 차량 리스트 호출 API
@api_car.route('/api/car-list', methods=['GET'])
def getCarList():
    page = int(request.args.get('page'))
    orderType = request.args.get('order')
    print(orderType)
    limit = 16
    offset = (page - 1) * limit
    car_list = []
    if(orderType == None):
        car_list = list(db.carInfo.find({}, {'_id': False}).sort('car_age', -1).limit(limit).skip(offset))
    else:
        arr = orderType.split('-')
        sortNm = 'car_age'
        sortType = 1 if arr[1] == 'asc' else -1
        ignore = {}
        if arr[0]=='price':
            sortNm = 'car_price'
            ignore = {'car_price': {'$ne': 0}}
        elif arr[0] == 'fuel':
            sortNm = 'car_fuel_basic'
            ignore = {'car_fuel_basic': {'$ne': 0}}
        print(page, sortNm, sortType)
        car_list = list(db.carInfo.find(ignore, {'_id': False}).sort(sortNm, sortType).limit(limit).skip(offset))

    return jsonify({"success": True, "carList": car_list})


@api_car.route('/car/detail')
def detail():
    return render_template('detail.html')
