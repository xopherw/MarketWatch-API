from flask import Flask, request, abort, jsonify, Response, json
from marketwatch import marketwatch as MW

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

@app.route('/stock/finance')
def finance():
    ticker = request.args.get('ticker', default='')
    period = request.args.get('period', default='annual')
    if(ticker == ''): abort(406, "ticker parameter cannot left blank!")
    if(period not in ['annual', 'quarter']): period = 'annual'
    return{
        "initiate"  :   "Inidivisual stock financial data.",
        "ticker"    :   f"{ticker}".upper(),
        'period'    :   f"{period}",
        "metadata"  :   'data.data()'
    }


class Error:

    def call(message, code):
        error_dict = {
            "code"      :   code,
            "message"   :   message
        }
        return error_dict, code

    def connection_error():
        message = "connection error."
        return Error.call(message, 500)

    def bad_request(req):
        message = f"{req} is either empty, or bad value."
        return Error.call(message, 400)


if(__name__ == "__main__"):
    app.run(debug=True)