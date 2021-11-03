from flask import Flask, request, abort, jsonify, Response, json
from marketwatch import marketwatch as MW
from error import Error

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/stock')
def ticker():
    ticker = request.args.get('ticker', default='')
    data = MW(ticker).data()
    json_data = {
        "initiate"  :   "Inidivisual stock data.",
        "ticker"    :   f"{ticker}".upper(),
        "metadata"  :   data
        }
    if(data == 500):
        return Error.connection_error()
    elif(data == 400):
        return Error.bad_request('ticker')
    else:
        return json_data

@app.route('/stock/financial')
def finance():
    ticker = request.args.get('ticker', default='')
    period = request.args.get('period', default='annual')
    finance = request.args.get('finance', default='income')
    data = MW(ticker).financial_data(finance, period)
    json_data = {
        "initiate"  :   "Inidivisual stock financial data.",
        "ticker"    :   f"{ticker}".upper(),
        "metadata"  :   data
    }
    if(data == 500):
        return Error.connection_error()
    elif(data == 400):
        return Error.ca('ticker')
    else:
        return json_data

if(__name__ == "__main__"):
    app.run(debug=True)