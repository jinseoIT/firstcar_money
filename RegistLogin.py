from flask import jsonify, request
from datetime import datetime, timedelta
import jwt
import os
from pymongo import MongoClient
import bcrypt
from dotenv import load_dotenv

load_dotenv(verbose=True)
jwtAlgorithm = os.getenv('JWT_ALGORITHM')
jwtKey = os.getenv('JWT_KEY')
dbId = os.getenv('DB_ADMIN_ID')
dbPw = os.getenv('DB_ADMIN_PW')

client = MongoClient(
    'mongodb+srv://' + dbId + ':' + dbPw + '@firstcar-money.ojfbk.mongodb.net/firstcar-money?retryWrites=true&w'
                                           '=majority')
db = client.firstcar

    # 유저가 입력한 아이디, 패스워드
def check_Regist(user_Email,user_Nick,user_PassWord,PassWord_Access):

    # 비밀번호가 일치하지 않는 경우
    if user_PassWord != PassWord_Access:
        return jsonify({'Success': False, 'msg': '비밀번호가 일치하지 않습니다'})
    # 이메일이 이미 존재하는 경우
    else:
        user = db.Users.find_one({"user_Email": user_Email}, {'_id': False})
        if user:

            return jsonify({'Success': False, 'msg': '이미 존재하는 이메일 입니다'})
        # 닉네임이 이미 존재하는 경우
        else:
            user = db.Users.find_one({"user_Nick": user_Nick}, {'_id': False})
            if user:
                return jsonify({'Success': False, 'msg': '이미 존재하는 닉네임 입니다'})
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
                return jsonify ({'Success': True, 'msg': '가입 되었습니다'})

def check_Login(user_Email,user_PassWord):

    user = db.Users.find_one({"user_Email": user_Email})
    # 아이디 혹은 비밀번호가 틀릴때
    if user == None:
        return jsonify({"Success": False, 'msg': '아이디 혹은 비밀번호가 잘못되었습니다'})
    # 해쉬된 비밀번호와 비교
    else:
        user_Nick = user["user_Nick"]
        user_PassWord = user_PassWord.encode('utf-8')
        result = bcrypt.checkpw(user_PassWord, user['user_PassWord'])
        # 비밀번호가 맞지 않을 경우
        if result == False:
            return jsonify({"Success": False, 'msg': '아이디 혹은 비밀번호가 잘못되었습니다'})
        # 로그인에 성공하여 토큰 부여
        else:
            user_id = (str(user["_id"]))
            jwtPayload = {
                "id": user_id,
                "nick": user_Nick,
                'exp': datetime.utcnow() + timedelta(seconds=60)
            }

            Token = jwt.encode(jwtPayload, jwtKey, jwtAlgorithm)
            # .decode('utf8')

            userInfo = { 'userId': user_id, 'userName' : user['user_Nick']}


            return jsonify({"success": True, "Token": Token, "userInfo": userInfo})