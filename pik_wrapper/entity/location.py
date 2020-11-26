from pik_wrapper.entity.entity import Entity


class Location(Entity):
    """
    :type name: str
    :type sort: int
    """

    def __init__(self, id_or_dict, name: str = None, sort: int = None):
        super().__init__(id_or_dict)
        if type(id_or_dict) is dict:
            name = id_or_dict.get('name')
            sort = id_or_dict.get('sort')
        if type(name) is not str:
            raise ValueError
        self.name = name
        if type(sort) is not int:
            raise ValueError
        self.sort = sort
