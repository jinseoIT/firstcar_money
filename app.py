from pymongo import MongoClient
from flask import Flask, render_template, request

import os
from dotenv import load_dotenv

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


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
