import json

from flask import request, Blueprint, Flask, render_template, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import random
import os

app = Flask(__name__)
load_dotenv(verbose=True)

dbId = os.getenv('DB_ADMIN_ID')
dbPw = os.getenv('DB_ADMIN_PW')

client = MongoClient(
    'mongodb+srv://' + dbId + ':' + dbPw + '@firstcar-money.ojfbk.mongodb.net/firstcar-money?retryWrites=true&w'
                                           '=majority')
db = client.firstcar

app_money = Blueprint('api_money', __name__, template_folder="templates")


@app_money.route('/car/from-range')
def your_money():

    user_car = list(db.carInfo.find({'car_price': {"$gte": 2000, "$lte": 3000}}).limit(40))

    if len(user_car) < 5:
        carList = random.sample(user_car, len(user_car))
    else:
        carList = random.sample(user_car, 5)
    carInfo = carList[0]
    carList.pop(0)
    return render_template('moneycar.html', carList = carList, carInfo = carInfo)



# 연봉별 차량조회 API[test]
@app_money.route('/api/car/from-range', methods=['GET'])
def getCarList_byMoney():
    user_min_money = request.args.get("min-money")
    carList = []

    if user_min_money:
        user_min_money = int(user_min_money)
        user_max_money = user_min_money + 1000

        user_car = list(
            db.carInfo.find({'car_price': {"$gte": user_min_money, "$lte": user_max_money}}).limit(40))

    if len(user_car) < 5:
        carList = random.sample(user_car, len(user_car))
    else:
        carList = random.sample(user_car, 5)

        for _list in carList:
            _list["_id"] = str(_list["_id"])

    return jsonify({"carList": carList})