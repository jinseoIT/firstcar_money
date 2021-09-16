from flask import render_template, Blueprint, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
import os


api_car = Blueprint('api_car', __name__, template_folder="templates")


dbId = os.getenv('DB_ADMIN_ID')
dbPw = os.getenv('DB_ADMIN_PW')

client = MongoClient('mongodb+srv://' + dbId + ':' + dbPw + '@firstcar-money.ojfbk.mongodb.net/firstcar-money?retryWrites=true&w'
            '=majority')
db = client.dbfirtcar

# 차량 리스트 페이지
@api_car.route('/car/list')
def home():
    page = int(request.args.get('page', 1))
    limit = 16
    offset = (page - 1) * limit
    # default 출시순 desc
    car_list = list(db.carInfo.find({}).sort('car_age', -1).limit(limit).skip(offset))
    for _list in car_list:
            _list["_id"] = str(_list["_id"])

    return render_template('carList.html', carList=car_list)

# 차량 리스트 호출 API
@api_car.route('/api/car-list', methods=['GET'])
def getCarList():
    page = int(request.args.get('page'))
    orderType = request.args.get('order')

    limit = 16
    offset = (page - 1) * limit
    car_list = []
    if(orderType == None):
        car_list = list(db.carInfo.find({}).sort('car_age', -1).limit(limit).skip(offset))
        for carinfo in car_list:
            carinfo["_id"] = str(carinfo["_id"])
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

        car_list = list(db.carInfo.find(ignore).sort(sortNm, sortType).limit(limit).skip(offset))
        for carinfo in car_list:
            carinfo["_id"] = str(carinfo["_id"])

    return jsonify({"success": True, "carList": car_list})


@api_car.route('/car/detail/<keyword>')
def detail(keyword):
    carId = keyword
    carInfo = db.carInfo.find_one({'_id': ObjectId(carId)})
    carInfo["_id"] = str(carInfo["_id"])
    return render_template('detail.html', carInfo= carInfo)

@api_car.route('/api/carInfo-check', methods=['POST'])
def checking():
    carId_receive = request.form['carId_give']
    carInfos = list(db.carInfo.find({'_id': ObjectId(carId_receive)}))
    for carinfo in carInfos:
            carinfo["_id"] = str(carinfo["_id"])
    print(carInfos)
    return jsonify({"success": True, "carInfo" : carInfos})

