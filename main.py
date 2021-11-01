from flask import Flask, request, abort, jsonify
from marketwatch import marketwatch as MW

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/stock')
def ticker():
    ticker = request.args.get('ticker', default='')
    if(ticker == ''): return Error.required('ticker')

    data = MW(ticker)
    return {
        "initiate"  :   "Inidivisual stock data.",
        "ticker"    :   f"{ticker}".upper(),
        "metadata"  :   data.data()
        }

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

    def required(req):
        return {
            "code"      :   400,
            "message"   :   f"{req} parameter is required."
        }

if(__name__ == "__main__"):
    app.run(debug=True)