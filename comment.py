from flask import Flask, jsonify, render_template, request, Blueprint
from dotenv import load_dotenv
from bson.objectid import ObjectId

api_comment = Blueprint('api_comment', __name__, template_folder="templates")

# 몽고 DB 연결
# import os
# load_dotenv(verbose=True)
# dbId = os.getenv('DB_ADMIN_ID')
# dbPw = os.getenv('DB_ADMIN_PW')

#  팀 프로젝트 공용 DB
# client = MongoClient(
#     'mongodb+srv://' + dbId + ':' + dbPw + '@firstcar-money.ojfbk.mongodb.net/firstcar-money?retryWrites=true&w'
#                                            '=majority')
# db = client.dbfirtcar
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.test

############ 몽고 DB 연습 ###############
## 1. Create : doc를 만들어서 몽고클라이언트에 넣기
# doc = {
#     'name':'kyusikko','age':21
# }
# db.comment.insert_one(doc)
## 2. Find : db에 있는 정보들을 찾아오기
# same_ages = list(db.comment.find({'age':21}, {'_id' : False}))
# print(same_ages)
## 3. Delete : 조건에 맞는 정보들을 지우기
# db.comment.delete_one({'name' : 'kyusikko'})


####### 클라에서 보낸 데이터 받아서 db에 저########
@api_comment.route('/api/comment-add', methods=['POST'])

def saving():
    nickname_receive = request.form['nickname_give'];
    comment_receive = request.form['comment_give'];
    currentTime_receive = request.form['currentTime_give'];




    # 몽고 db에 들어갈 데이터 양식
    doc = {
        "nickname" : nickname_receive,
        "comment" : comment_receive,
        "currentTime" : currentTime_receive,
    }

    # 몽고 db에 저장!
    db.comment.insert_one(doc)
    return jsonify({"success": True, 'msg': '요청이 보내졌습니다.'})



########## 클라가 요청 보내면 데이터베이스에 있던 댓글들 다 보내주기 ##########
@api_comment.route('/api/comment-list', methods=['GET'])
def listing():
    # db에서 가져올때 최신순으로 가져오는 것을 한번 찾아보자.
    # comment_lists = list(db.comment.find({ }))
    comment_lists = list(db.comment.find({ }))
    for comment_list in comment_lists:
        comment_list["_id"] = str(comment_list["_id"])

    return jsonify({"success": True, 'comment': comment_lists})



# 댓글 삭제

@api_comment.route('/api/comment-delete', methods=['POST'])
def deleting():
    id_receive = request.form['id_give']
    # print(id_receive)
    # 이거 어떻게 돌아가누
    result = db.comment.delete_one({'_id': ObjectId(id_receive)})
    # test = db.comment.delete_one({'_id' : id_receive})
    # test = db.comment.delete_one({'_id': {"$oid": str(id_receive)}})
    print(result)
    return jsonify({"success": False, 'msg' : '삭제 완료했습니다.'})


# # 댓글 수정
@api_comment.route('/api/comment-modi', methods=['POST'])
def modifing():
    id_receive = request.form['id_give']
    # print(id_receive)
    # 이거 어떻게 돌아가누
    result = list(db.comment.find({'_id': ObjectId(id_receive)}, {'_id': False}))
    # test = db.comment.delete_one({'_id' : id_receive})
    # test = db.comment.delete_one({'_id': {"$oid": str(id_receive)}})
    print(result)
    return jsonify({"success": False, "result" : result})





