from flask import Flask
from flask import render_template, url_for
app = Flask(__name__)


# TEMPLATES = "templates/" #goes here by default


@app.route("/")
def defaultRoute():
    # url_for('static', filename='main.css')
    return render_template("index.html")