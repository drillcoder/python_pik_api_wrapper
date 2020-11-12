class ValueObject:
    def __repr__(self):
        return ', '.join(f'{item}: {getattr(self, item)}' for item in self.__dict__)
