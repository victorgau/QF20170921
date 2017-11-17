import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    message = """請在網址列上選擇要看的公司名單：<br/>
    /nasdaq ==> nasdaq 的公司名單<br/>
    /nyse ==> nyse 的公司名單<br/>
    /amex ==> amex 的公司名單<br/>
    """
    return message

@app.route('/nyse')
def nyse():
    # TODO:"請填入合適的程式碼！"
    return "Hello!!!"

@app.route('/nyse/<symbol>')
def nyse_company(symbol):
    # TODO:"請填入合適的程式碼！"
    return "Hello!!!"

@app.route('/nasdaq')
def nasdaq():
    # TODO:"請填入合適的程式碼！"
    return "Hello!!!"

@app.route('/nasdaq/<symbol>')
def nasdaq_company(symbol):
    # TODO:"請填入合適的程式碼！"
    return "Hello!!!"

@app.route('/amex')
def amex():
    # TODO:"請填入合適的程式碼！"
    return "Hello!!!"

@app.route('/amex/<symbol>')
def amex_company(symbol):
    # TODO:"請填入合適的程式碼！"
    return "Hello!!!"


if __name__=="__main__":
    app.run()
