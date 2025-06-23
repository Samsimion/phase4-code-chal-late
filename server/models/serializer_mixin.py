class SerializerMixin:
    def to_dict(self):
        result = {}
        for column in self.__table__.columns:
            result[column.name] = getattr(self, column.name)
        return result
