from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = randint(1, 10)
    this_year = datetime.now().year
    return render_template("index.html", num=random_number, year=this_year)

@app.route("/guess/<name>")
def guess(name):
    respons = requests.get(f"https://api.agify.io?name={name}")
    gender_res = requests.get(f"https://api.genderize.io?name={name}")
    age = respons.json()["age"]
    gender = gender_res.json()["gender"]

    return f"<h1>Hey {name},<h1>" \
        f"<h2>I think you are {gender},</h2>" \
            f"<h2>And maybe {age} years old.</h2>"



if __name__ == "__main__":
    app.run(debug=True)