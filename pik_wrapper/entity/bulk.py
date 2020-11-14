from pik_wrapper.entity.entity import Entity


class Bulk(Entity):
    def __init__(self, id: str, name: str, sort: int, type_id: int):
        super().__init__(id)
        if type(name) is not str:
            raise ValueError
        self.name = name
        if type(sort) is not int:
            raise ValueError
        self.sort = sort
        if type(type_id) is not int:
            raise ValueError
        self.type_id = type_id
