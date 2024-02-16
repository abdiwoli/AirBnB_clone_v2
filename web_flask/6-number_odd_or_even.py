#!/usr/bin/python3
""" import modules """
from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ main page """
    return "Hello HBNB!"


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ render """
    return render_template("6-number_odd_or_even.html", number=n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ render """
    return render_template("5-number.html", number=n)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ hbnb view """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ c is fun """
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """ python is cool """
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """ is number  """

    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
