import pandas as pd
from flask import Flask


app = Flask(__name__)

@app.route("/averagehigh")
def calculate_average():
    df = pd.read_csv('hw.csv')
    result = df.sum()/df.shape[0]
    return result



