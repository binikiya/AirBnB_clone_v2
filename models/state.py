#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """get list of City instances with state_id equals to the current State.id"""
        list_cities = []
        all_cities = models.storage.all(City)
        for key, city_obj in all_cities.items():
            if city_obj.state_id == self.id:
                list_cities.append(city_obj)
        return list_cities
