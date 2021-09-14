from flask import Flask, render_template, Blueprint

app = Flask(__name__)

app_account = Blueprint('api_account', __name__, template_folder="templates")

# main
@app_account.route('/test')
def home():
    return render_template('account.html')
