#!/usr/bin/python3
""" import modules """

from flask import Flask, jsonify, render_template
from markupsafe import escape
from models import HBNB_TYPE_STORAGE, storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ sates list"""
    if id is None:
        states_list = [st for st in storage.all("State").values()
                       if st is not None]
    else:
        states_list = [st for st in storage.all(State).values() if st.id == id]
    if len(states_list) > 0:
        return render_template(
            '9-states.html', states=states_list, id=id)
    else:
        return render_template('9-states.html', id=id)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ close sesion """
    print("Teardown app context called.")
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
