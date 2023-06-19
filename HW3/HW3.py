
import requests

import pandas as pd

from flask import Flask, request
from faker import Faker
from flask_jsonpify import jsonpify
from webargs import fields, validate

from webargs.flaskparser import use_args

app = Flask(__name__)

fake = Faker("UK")
@app.route("/generate-students")
@use_args(
    {
        "counter": fields.Int(
            missing=0,
            validate=[validate.Range(min=1, max=1000)]
        )
    },
    location="query"
)
def generate_students(counter):
    data = {
        "Name": [],
        "Date": [],
        "Email": [],
        "Password": []
    }
    for i in range(counter['counter']):
        data["Name"].append(fake.name())
        data["Date"].append(str(fake.date_between(start_date='-60y', end_date='-17y')))
        data["Email"].append(fake.email())
        data["Password"].append(fake.password())
    df = pd.DataFrame(data, columns=['Name', 'Date', 'Email', 'Password'])
    df_list = df.values.tolist()
    jsonp_data = jsonpify(df_list)
    df.to_csv("students.csv")
    return jsonp_data

@app.route("/bitcoin_rate/")
@use_args(
    {
        "currency": fields.Str(
            load_default='USD'
        ),
        "convert": fields.Int(
            missing=1
        )
    },
    location="query"
)
def get_bitcoin_value(currency):
    url = 'https://bitpay.com/api/rates'
    symbol_url = 'https://test.bitpay.com/currencies'
    symbol_result = requests.get(symbol_url, {}).json()
    result = requests.get(url, {}).json()
    symbol = [element['symbol'] for element in symbol_result['data'] if element['code'] == currency['currency']]
    return str([element['rate']*float(currency['convert']) for element in result if element['code']
                == currency['currency']]).replace('[','').replace(']', '')+str(symbol)

if __name__ == "__main__":
    app.run(debug=True)
