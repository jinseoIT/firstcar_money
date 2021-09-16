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
db = client.dbfirtcar

app_money = Blueprint('api_money', __name__, template_folder="templates")


@app_money.route('/car/from-range')
def your_money():
    user_min_money = request.args.get("min-money")
    if user_min_money:

        user_min_money = int(user_min_money.replace(",", "").replace("만원",""))
        user_max_money = user_min_money + 1000

        user_car = list(db.carInfo.find({'car_price': {"$gte": user_min_money, "$lte": user_max_money}}))

        if len(user_car) < 5:
            car_5 = random.sample(user_car, len(user_car))
        else:
            car_5 = random.sample(user_car, 5)

        return render_template('moneycar.html', data=car_5)
    else:

        return render_template('moneycar.html')



# 연봉별 차량조회 API[test]
@app_money.route('/api/car/by-money', methods=['GET'])
def getCarList_byMoney():
    print('타나')
    #limit = 5
    car_list = list(db.carInfo.find({"car_price": {"$gt": 2000, "$lt":3000}}, {'_id': False}))

    return jsonify({"success": True, "carList": car_list})