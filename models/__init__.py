#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBStorage"""

from os import getenv

HBNB_TYPE_STORAGE = getenv("HBNB_TYPE_STORAGE")

if HBNB_TYPE_STORAGE == 'db':
    from .engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from .engine.file_storage import FileStorage
    storage = FileStorage()
from .base_model import BaseModel, Base
from .state import State
from .city import City
from .review import Review
from .user import User
from .amenity import Amenity
from .place import Place

storage.reload()
