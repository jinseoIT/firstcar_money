from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


# main
@app.route('/test')
def home():
    return render_template('account.html')
