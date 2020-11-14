from typing import List

from pik_wrapper.entity.entity import Entity
from pik_wrapper.value_object.photo import Photo


class Item(Entity):
    def __init__(self, id: str, public_date: str, date: str, photos: List[Photo]):
        super().__init__(id)
        if type(public_date) is not str:
            raise ValueError
        self.public_date = public_date
        if type(date) is not str:
            raise ValueError
        self.date = date
        if type(photos) is not list:
            raise ValueError
        self.photos = photos
