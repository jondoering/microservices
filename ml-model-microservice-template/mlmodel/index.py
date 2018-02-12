# main file for RESTful API

from flask import Flask, jsonify, request


app = Flask(__name__)

#GET for getting model description
@app.route("/description")
def get_description():
    '''
    prints a basic description of the implemented ML algorithm
    within this container.
    :return:
    '''
    print("ToDo")
    pass

#GET for getting current model outcome
@app.route("/result")
def get_result():
    '''
    returns the output of the current machine learning algorithm
    respecitvely a
    :return:
    '''
    print("ToDo")
    pass


#
@app.route("/data", methods=['POST'])
def post_data():
    '''
    Allows to push data into the ML algorithm. The data should
    be packaged as a data frame and structured in a way,
    the ml algo can use it.

    :return:
    '''
    print("ToDo")
    pass


@app.route("/data", methods=['GET'])
def get_data():
    '''
    allows to fetch current data
    :return:
    '''
    print("ToDo")
    pass

