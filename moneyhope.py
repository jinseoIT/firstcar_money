from flask import request,Blueprint,Flask,render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os
app = Flask(__name__)
load_dotenv(verbose=True)

dbId = os.getenv('DB_ADMIN_ID')
dbPw = os.getenv('DB_ADMIN_PW')

client = MongoClient(
    'mongodb+srv://' + dbId + ':' + dbPw + '@firstcar-money.ojfbk.mongodb.net/firstcar-money?retryWrites=true&w'
                                           '=majority')
db = client.dbfirtcar

app_money = Blueprint('api_money',__name__, template_folder="templates")
@app_money.route('/money/cars')
def your_money():
    user_Money = request.args.get("money")
    cars = []
    hope_cars = []
    if user_Money:
        user_price = int(user_Money.replace(",", ""))
        max_price = user_price + 1000
        
        user_car = db.carInfo.find({})
        for doc in user_car:
          
          if doc["car_price"] == 0 :
              pass
          elif doc["car_price"] =="":
              pass
          else:       
             doc["car_price"] = int( doc["car_price"])
             
             cars.append(doc)

        for new_doc in cars :
           if  max_price<new_doc["car_price"]:
               pass
           else:
               hope_cars.append(new_doc)
        print(hope_cars)
        return render_template('moneycar.html')
    else:

        return render_template('moneycar.html')

