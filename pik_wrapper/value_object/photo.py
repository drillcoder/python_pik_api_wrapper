from pik_wrapper.value_object.value_object import ValueObject


class Photo(ValueObject):
    """
    :type url_or_dict: str
    :type sort: int
    """
    def __init__(self, url_or_dict, sort: int = None):
        url = url_or_dict
        if isinstance(url_or_dict, dict):
            url = url_or_dict.get('url')
            sort = url_or_dict.get('sort')
        if type(url) is not str:
            raise ValueError
        self.url = url
        if type(sort) is not int:
            raise ValueError
        self.sort = sort
