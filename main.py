import string
import random

from flask import Flask

app = Flask(__name__)

@app.route("/")
def generate_password():
    return "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.punctuation +string.digits,
                          k=random.randint(10, 20)))


if __name__ == '__main__':
    app.run()
generate_password()

