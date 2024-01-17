#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    amenity_ids = []

    # Define relationships
    reviews = relationship(
            "Review", backref="place", cascade="all, delete-orphan"
            )

    # Define the Many-To-Many relationship with Amenity
    amenities = relationship(
            "Amenity", secondary="place_amenity",
            viewonly=False, back_populates="place_amenities"
            )

    # Additional code for FileStorage
    @property
    def reviews(self):
        """ Getter attribute for reviews in FileStorage """
        from models import storage
        reviews_list = []
        for review in storage.all("Review").values():
            if review.place_id == self.id:
                reviews_list.append(review)
        return reviews_list

    @property
    def amenities(self):
        """ Getter attribute for amenities in FileStorage """
        from models import storage
        amenity_list = []
        for amenity in storage.all("Amenity").values():
            if amenity.id in self.amenity_ids:
                amenity_list.append(amenity)
        return amenity_list

    @amenities.setter
    def amenities(self, obj):
        """ Setter attribute for amenities in FileStorage """
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)
