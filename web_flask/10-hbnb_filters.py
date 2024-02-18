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


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ sates list"""
    states_list = sorted(list(storage.all("State").values()),
                         key=lambda x: x.name)
    amenity = [st for st in storage.all("Amenity").values() if st.name is not None]
    print(amenity)

    return render_template('10-hbnb_filters.html', states=states_list, amenities=amenity)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
