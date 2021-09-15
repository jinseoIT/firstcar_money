from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify, make_response, redirect

import os
from dotenv import load_dotenv

import RegistLogin
import account
import car
import moneyhope

load_dotenv(verbose=True)

dbId = os.getenv('DB_ADMIN_ID')
dbPw = os.getenv('DB_ADMIN_PW')

app = Flask(__name__)
app.register_blueprint(car.api_car)
app.register_blueprint(account.app_account)
app.register_blueprint(account.app_login)
app.register_blueprint(moneyhope.app_money)

client = MongoClient(
    'mongodb+srv://' + dbId + ':' + dbPw + '@firstcar-money.ojfbk.mongodb.net/firstcar-money?retryWrites=true&w'
                                           '=majority')
db = client.dbfirtcar


# main
@app.route('/')
def home():
    return render_template('main.html')


@app.route('/user/emailChk')
def email_Chk():
    return render_template('index.html')


@app.route('/user/nicknameChk')
def nickname_Chk():
    return render_template('index.html')


@app.route('/user/login')
def login_User():
    return render_template('login.html')


@app.route('/user/register')
def register_User():
    return render_template('register.html')


@app.route("/user/register_Process", methods=['POST'])
def register_Process_User():
    user_Datas = request.get_json()
    # 유저가 입력한 아이디, 패스워드
    user_Email = user_Datas["Email"]
    user_Nick = user_Datas["Nick"]
    user_PassWord = user_Datas["PassWord"]
    PassWord_Access = user_Datas["PassWord_Access"]
    res = RegistLogin.check_Regist(user_Email, user_Nick, user_PassWord, PassWord_Access)
    return res


@app.route('/car/list', methods=['GET'])
def getCarList():
    page = int(request.args.get('page', 1))
    limit = 10
    offset = (page - 1) * limit
    car_list = list(db.carInfo.find({}, {'_id': False}).limit(limit).skip(offset))
    print('왜안되나영')
    return jsonify({"success": False, "car_list": car_list})



@app.route('/user/logout', methods=['GET'])
def logout():
    resp = make_response(render_template('main.html'))
    resp.delete_cookie('token')
    return resp


@app.route('/detail')
def detail():
    return render_template('detail.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
