#!/usr/bin/python3
""" import modules """
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def index():
    """ main page """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ main page """
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
