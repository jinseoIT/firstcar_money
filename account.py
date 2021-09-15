from flask import Flask, Blueprint, request
import RegistLogin
app = Flask(__name__)

app_account = Blueprint('api_account', __name__, template_folder="templates")
app_login = Blueprint('api_login',__name__, template_folder="templates")
# main
@app_account.route("/user/register-Process", methods=['POST'])
def register_Process_User():
    user_Datas = request.get_json()
    # 유저가 입력한 아이디, 패스워드
    user_Email = user_Datas["Email"]
    user_Nick = user_Datas["Nick"]
    user_PassWord = user_Datas["PassWord"]
    PassWord_Access = user_Datas["PassWord_Access"]
    res = RegistLogin.check_Regist(user_Email,user_Nick,user_PassWord,PassWord_Access)
    return res

@app_login.route('/user/login-Process', methods=['POST'])
def login_Process_User():
    user_Datas = request.get_json()
    # 유저가 입력한 아이디, 패스워드
    user_Email = user_Datas["Email"]
    user_PassWord = user_Datas["PassWord"]
    res = RegistLogin.check_Login(user_Email,user_PassWord)
    return res
