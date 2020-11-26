from typing import List

from pik_wrapper.entity.entity import Entity
from pik_wrapper.value_object.photo import Photo


class Item(Entity):
    """
    :type public_date: str
    :type date: str
    :type photos: List[Photo]
    """
    def __init__(self, id_or_dict, public_date: str = None, date: str = None, photos: List[Photo] = list):
        super().__init__(id_or_dict)
        if type(id_or_dict) is dict:
            public_date = id_or_dict.get('public_date')
            date = id_or_dict.get('date')
            photos = id_or_dict.get('photos', [])
        if type(public_date) is not str:
            raise ValueError
        self.public_date = public_date
        if type(date) is not str:
            raise ValueError
        self.date = date
        if type(photos) is not list:
            raise ValueError
        self.photos = photos
