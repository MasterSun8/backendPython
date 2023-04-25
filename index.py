from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    file = open("data.txt")
    return file.read()

@app.route("/help")
def help():
    return "This is a help message"

@app.route("/welp")
def welp():
    return "This is a welp message"

@app.route("/add")
def add():
    file = open("data.txt", "r+")
    count = file.read()
    if(count):
        count = int(count)
        count += 1
        file.truncate(0)
        file.seek(0)
    else:
        count = 1
    file.write(str(count))
    file.close()
    return "Added success"

@app.route("/clear")
def clear():
    file = open("data.txt", "w").close()
    return "File cleared"