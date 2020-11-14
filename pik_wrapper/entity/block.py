from pik_wrapper.entity.entity import Entity


class Block(Entity):
    def __init__(self, id: str, name: str, sort: int):
        super().__init__(id)
        if type(name) is not str:
            raise ValueError
        self.name = name
        if type(sort) is not int:
            raise ValueError
        self.sort = sort
