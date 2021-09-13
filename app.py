from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
<<<<<<< HEAD
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)
dbId = os.getenv('DB_ADMIN_ID')
dbPw = os.getenv('DB_ADMIN_PW')

=======

import account
>>>>>>> de009fb51746623f24dc058efaa192a141aa2786

app = Flask(__name__)

#client = MongoClient('localhost', 27017)
#db = client.firstcar_money
client = MongoClient('mongodb+srv://'+dbId+':'+dbPw+'@firstcar-money.ojfbk.mongodb.net/firstcar-money?retryWrites=true&w'
                     '=majority')
db = client.dbfirtcar



# main
@app.route('/')
def home():
    return render_template('index.html')

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

    user_Email = user_Datas["Email"]
    user_Nick = user_Datas["Nick"]
    user_PassWord = user_Datas["PassWord"]
    PassWord_Access = user_Datas["PassWord_Access"]

    if user_PassWord != PassWord_Access :
        return jsonify({'Error':'passWord_Error','msg':'비밀번호가 일치하지 않습니다'})

    else :
        user=db.Users.find_one({"user_Email":user_Email}, {'_id': False})
        if user :
            return jsonify({'Error': 'Email_Error', 'msg': '이미 존재하는 이메일 입니다'})
        else:
            user=db.Users.find_one({"user_Nick":user_Nick}, {'_id': False})
            if user:
               return jsonify({'Error': 'Nick_Error', 'msg': '이미 존재하는 닉네임 입니다'})

    # doc = {
    #     user_Email,
    #     user_Nick,
    #
    #
    # }
    # db.Users.insert_one(doc)

<<<<<<< HEAD
@app.route('/car/list', methods=['GET'])
def getCarList():
    page = int(request.args.get('page', 1))
    limit = 10
    offset = (page-1) * limit
    car_list = list(db.carInfo.find({}, {'_id': False}).limit(limit).skip(offset))
    print('왜안되나영')
    return jsonify({ "success": False , "car_list" : car_list })
=======
>>>>>>> de009fb51746623f24dc058efaa192a141aa2786





if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
