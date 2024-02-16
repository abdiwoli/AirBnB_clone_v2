#!/usr/bin/python3
""" import modules """
from flask import Flask, jsonify
from markupsafe import escape
from models import HBNB_TYPE_STORAGE, storage
from models.state import State

app = Flask(__name__)


@app.route('/')
def index():
    states = storage.all(State).values()
    states_list = [state.to_dict() for state in states]
    return jsonify(states_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
