#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models import HBNB_TYPE_STORAGE


class State(BaseModel, Base):
    """ state """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if HBNB_TYPE_STORAGE != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            from models import storage
            city_list = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
