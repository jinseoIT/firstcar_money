from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

import os
from dotenv import load_dotenv
load_dotenv(verbose=True)
dbId = os.getenv('DB_ADMIN_ID')
dbPw = os.getenv('DB_ADMIN_PW')



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
    # 유저가 입력한 아이디, 패스워드
    user_Email = user_Datas["Email"]
    user_Nick = user_Datas["Nick"]
    user_PassWord = user_Datas["PassWord"]
    PassWord_Access = user_Datas["PassWord_Access"]

    reg_E = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    reg_user_Email = reg_E.match(user_Email)
    # 이메일 형식이 아닌 경우
    if reg_user_Email == None:

        return jsonify({"Success": False, 'msg': '이메일 형식으로 입력해 주세요'})
    # 닉네임, 패스워드, 패스워드 확인 칸이 비어있을 경우
    elif ""==user_Nick or ""==user_PassWord or ""==PassWord_Access :
        return jsonify({"Success": False, 'msg': '입력란을 모두 입력해 주세요'})
    
    # 비밀번호가 일치하지 않는 경우
    elif user_PassWord != PassWord_Access:
        return jsonify({'Error': 'passWord_Error', 'msg': '비밀번호가 일치하지 않습니다'})
    # 이메일이 이미 존재하는 경우
    else:
        user = db.Users.find_one({"user_Email": user_Email}, {'_id': False})
        if user:

            return jsonify({'Error': False, 'msg': '이미 존재하는 이메일 입니다'})
        # 닉네임이 이미 존재하는 경우
        else:
            user = db.Users.find_one({"user_Nick": user_Nick}, {'_id': False})
            if user:
                return jsonify({'Error': False, 'msg': '이미 존재하는 닉네임 입니다'})
            # 회원가입 성공
            else:
                user_PassWord = user_PassWord.encode('utf-8')
                user_PassWord = bcrypt.hashpw(user_PassWord, bcrypt.gensalt())

                doc = {
                    "user_Email": user_Email,
                    "user_Nick": user_Nick,
                    "user_PassWord": user_PassWord
                }
                db.Users.insert_one(doc)
                return jsonify({'Success': True, 'msg': '가입 되었습니다'})



@app.route('/car/list', methods=['GET'])
def getCarList():
    page = int(request.args.get('page', 1))
    limit = 10
    offset = (page-1) * limit
    car_list = list(db.carInfo.find({}, {'_id': False}).limit(limit).skip(offset))
    print('왜안되나영')
    return jsonify({ "success": False , "car_list" : car_list })





if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
