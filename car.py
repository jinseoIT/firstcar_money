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
    car_list = list(db.carInfo.find({}, {'_id': False}).limit(limit).skip(offset))
    return render_template('carList.html', carList=car_list)

# 차량 리스트 호출 API
@api_car.route('/api/car-list', methods=['GET'])
def getCarList():
    page = int(request.args.get('page'))
    print('request :', request)
    print('page:', page)
    limit = 16
    offset = (page - 1) * limit
    car_list = list(db.carInfo.find({}, {'_id': False}).limit(limit).skip(offset))

<<<<<<< HEAD
    return jsonify({"success": True, "carList": car_list})
=======
    return jsonify({"success": False, "car_list": car_list})

@api_car.route('/car/detail')
def detail():
    return render_template('detail.html')
>>>>>>> 95d888cf955d47f6eaf9811801d9e7bf3618605d
