from pymongo import MongoClient
from flask import  Flask, render_template, request
import RegistLogin
import os
from dotenv import load_dotenv

import account
import car

load_dotenv(verbose=True)

dbId = os.getenv('DB_ADMIN_ID')
dbPw = os.getenv('DB_ADMIN_PW')

app = Flask(__name__)
app.register_blueprint(car.api_car)
app.register_blueprint(account.app_account)

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


@app.route('/user/login_Process', methods=['POST'])
def login_Process_User():
    user_Datas = request.get_json()
    # 유저가 입력한 아이디, 패스워드
    user_Email = user_Datas["Email"]
    user_PassWord = user_Datas["PassWord"]
    res = RegistLogin.check_Login(user_Email,user_PassWord)
    return res

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
    res = RegistLogin.check_Regist(user_Email,user_Nick,user_PassWord,PassWord_Access)
    return res


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
