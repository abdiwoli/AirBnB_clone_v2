#!/usr/bin/python3
""" import modules """
from flask import Flask, jsonify, render_template
from markupsafe import escape
from models import HBNB_TYPE_STORAGE, storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ close sesion """
    print("Teardown app context called.")
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """ sates list"""
    states_list = sorted(list(storage.all("State").values()),
                         key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
