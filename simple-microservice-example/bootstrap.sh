#!/bin/sh

export FLASK_APP=./cashman/index.py

#activate projects virtual environment
source $(pipenv --venv)/bin/activate

flask run -h 0.0.0.0