from pik_wrapper.value_object.value_object import ValueObject


class Photo(ValueObject):
    def __init__(self, url: str, sort: int):
        if type(url) is not str:
            raise ValueError
        self.url = url
        if type(sort) is not int:
            raise ValueError
        self.sort = sort
