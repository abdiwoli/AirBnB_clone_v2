#!/usr/bin/python3
""" import modules """
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def index():
    """ main page """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
