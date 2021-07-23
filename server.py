from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

app = Flask(__name__)

#dynamically adding our copyright year
@app.route("/")
def home():
    random_number = randint(1, 10)
    this_year = datetime.now().year
    return render_template("index.html", num=random_number, year=this_year)

#Using an api to guess a given route age and gender
@app.route("/guess/<name>")
def guess(name):
    respons = requests.get(f"https://api.agify.io?name={name}")
    gender_res = requests.get(f"https://api.genderize.io?name={name}")
    age = respons.json()["age"]
    gender = gender_res.json()["gender"]

    return f"<h1>Hey {name},<h1>" \
        f"<h2>I think you are {gender},</h2>" \
            f"<h2>And maybe {age} years old.</h2>"


# practicing passing multiple value into our templates in this blob route
@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    respons = requests.get(blog_url)
    all_post = respons.json()

    return render_template("blog.html", posts=all_post)

if __name__ == "__main__":
    app.run(debug=True)
