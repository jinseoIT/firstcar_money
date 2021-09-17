from datetime import datetime

from flask import Flask, jsonify, render_template, request, Blueprint
from dotenv import load_dotenv
from bson.objectid import ObjectId
from pymongo import MongoClient
import os
app = Flask(__name__)
api_like = Blueprint('api_like', __name__, template_folder="templates")

# 몽고 DB 연결
# import os
load_dotenv(verbose=True)
dbId = os.getenv('DB_ADMIN_ID')
dbPw = os.getenv('DB_ADMIN_PW')

#  팀 프로젝트 공용 DB
client = MongoClient(
     'mongodb+srv://' + dbId + ':' + dbPw + '@firstcar-money.ojfbk.mongodb.net/firstcar-money?retryWrites=true&w'
                                            '=majority')
db = client.firstcar.comments