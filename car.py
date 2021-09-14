from flask import render_template, Blueprint, request, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv

api_car = Blueprint('api_car', __name__, template_folder="templates")


dbId = os.getenv('DB_ADMIN_ID')
dbPw = os.getenv('DB_ADMIN_PW')

client = MongoClient(
    'mongodb+srv://' + dbId + ':' + dbPw + '@firstcar-money.ojfbk.mongodb.net/firstcar-money?retryWrites=true&w'
                                           '=majority')
db = client.dbfirtcar

@api_car.route('/carList')
def home():
    return render_template('carList.html')

@api_car.route('/api/carList', methods=['GET'])
def getCarList():
    page = int(request.args.get('page', 1))
    limit = 10
    offset = (page - 1) * limit
    car_list = list(db.carInfo.find({}, {'_id': False}).limit(limit).skip(offset))
    print('왜안되나영')
    return jsonify({"success": False, "car_list": car_list})