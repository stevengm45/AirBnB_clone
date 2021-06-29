#!/usr/bin/python3
"""
   This is the Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class Place that defines the place where the service is offer
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""
