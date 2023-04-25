from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "essa"

@app.route("/help")
def help():
    return "This is a help message"

@app.route("/welp")
def welp():
    return "This is a welp message"