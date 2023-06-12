import string
import random


from flask import Flask

app = Flask(__name__)

@app.route("/password")
def generate_password():
    return "".join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.punctuations+string.digits,
                          k=random.randint(10, 20)))



