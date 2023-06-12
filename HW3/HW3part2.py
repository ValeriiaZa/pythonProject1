import requests
from flask import Flask,request
app = Flask(__name__)

@app.route("/bitcoin_rate")
def get_bitcoin_value():
    url = 'https://bitpay.com/api/rates'
    result = requests.get(url, {}).json()
    cur_arg = request.args.get('currency', default='USD')
    return str([element['rate'] for element in result if element['code'] == cur_arg])
if __name__ == "__main__":
    app.run(debug=True)

