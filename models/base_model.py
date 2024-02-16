#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from models import HBNB_TYPE_STORAGE


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True, default= str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(
            DateTime, nullable=False, default=datetime.utcnow(),
            onupdate=datetime.utcnow()
            )

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                        kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'
                        )
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f'
                        )
            #del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.pop('_sa_instance_state', None)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        if 'created_at' in dictionary and isinstance(dictionary['created_at'], datetime):
            dictionary['created_at'] = dictionary['created_at'].isoformat()
        if 'updated_at' in dictionary and isinstance(dictionary['updated_at'], datetime):
            dictionary['updated_at'] = dictionary['updated_at'].isoformat()
        return dictionary

    def delete(self):
        """Deletes object from storage."""
        from models import storage
        storage.delete(self)
