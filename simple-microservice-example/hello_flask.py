#Testing Flask framework
#to execute in terminal:
# >export FLASK_APP=hello_flask
# >flask run

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "This is root folder"

@app.route("/endpoint1")
def hello_endpoint1():
    return "This is endpoint1 folder"

