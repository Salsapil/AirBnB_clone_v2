#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base, Column, String
from os import getenv
from models.amenity import Amenity

# Association table
place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
    ),
)


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
            "Review", cascade="all, delete", backref="place")
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            viewonly=False,
            backref="place_amenities",
        )
    else:

        @property
        def reviews(self):
            """FileStorage relationship between Place and Review"""
            from models import storage
            from models.review import Review

            rvs = []
            rvs_dict = storage.all(Review)
            for review in rvs_dict.values():
                if review.place_id == self.id:
                    rvs.append(review)
            return rvs

        @property
        def amenities(self):
            """Get Amenities list"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """set amenities Ids"""
            if isinstance(obj, Amenity) and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
