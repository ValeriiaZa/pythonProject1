import pandas as pd

from flask import Flask
from faker import Faker
from flask_jsonpify import jsonpify

app = Flask(__name__)

fake = Faker("UK")
@app.route("/<int:counter>/")
def generate_students(counter):
    if counter > 1000:
        return f'Error:Request limit exceeded. Try form (0, 1000)'
    data = {
        "Name": [],
        "Date": [],
        "Email": [],
        "Password": []
    }
    for i in range(int(counter)):
        data["Name"].append(fake.name())
        data["Date"].append(str(fake.date_between(start_date='-60y', end_date='-17y')))
        data["Email"].append(fake.email())
        data["Password"].append(fake.password())
    df = pd.DataFrame(data, columns=['Name', 'Date', 'Email', 'Password'])
    df_list = df.values.tolist()
    jsonp_data = jsonpify(df_list)
    df.to_csv("students.csv")
    return jsonp_data

if __name__ == "__main__":
    app.run(debug=True)
