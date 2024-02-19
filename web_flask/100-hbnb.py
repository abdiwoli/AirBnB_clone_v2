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


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ sates list"""
    states_list = [st for st in storage.all("State").values()
                   if st.name is not None]
    amenity = [st for st in storage.all("Amenity").values()
               if st.name is not None]
    places = [st for st in storage.all("Place").values()
               if st.name is not None]

    return render_template('100-hbnb.html',
                           states=states_list, amenities=amenity, places=places)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
