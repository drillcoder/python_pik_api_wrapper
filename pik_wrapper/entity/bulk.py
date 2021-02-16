from pik_wrapper.entity.entity import Entity


class Bulk(Entity):
    """
    :type name: str
    :type sort: int
    :type type_id: int
    :type settlement_fact: bool
    """

    def __init__(self, id_or_dict, name: str = None, sort: int = None, type_id: int = 0, settlement_fact: bool = None):
        super().__init__(id_or_dict)
        if type(id_or_dict) is dict:
            name = id_or_dict.get('name')
            sort = id_or_dict.get('sort')
            type_id = id_or_dict.get('type_id', 0)
            settlement_fact = bool(id_or_dict.get('settlement_fact', 0))
        if type(name) is not str:
            raise ValueError
        self.name = name
        if type(sort) is not int:
            raise ValueError
        self.sort = sort
        if type(type_id) is not int:
            raise ValueError
        self.type_id = type_id
        if type(settlement_fact) is not bool:
            raise ValueError
        self.settlement_fact = settlement_fact
