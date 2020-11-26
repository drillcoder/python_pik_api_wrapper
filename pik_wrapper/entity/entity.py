class Entity:
    """
    :type id: str
    """

    def __init__(self, id_or_dict):
        id = id_or_dict
        if type(id_or_dict) is dict:
            id = id_or_dict.get('id')
        if type(id) is not str:
            raise ValueError
        self.id = id

    def __repr__(self):
        str_list = []
        for item in self.__dict__:
            if type(getattr(self, item)) is list:
                elements = []
                for element in getattr(self, item):
                    elements.append(f'{element.__repr__()}')
                str_list.append(f'{item}:\n' + "\n".join(elements))
                continue
            str_list.append(f'{item}: {getattr(self, item)}')
        return ', '.join(str_list)
