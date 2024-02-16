#!/usr/bin/python3
""" import modules """
from flask import Flask, jsonify, render_template
from markupsafe import escape
from models import HBNB_TYPE_STORAGE, storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def index():
    states = storage.all(State).values()
    states_list = [state.to_dict() for state in states]
    return render_template('7-states_list.html', states=states_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
