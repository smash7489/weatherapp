from flask import Flask ,render_template  ,request
import requests

app = Flask(__name__)

def homepage():
    return render_template("index.html")








