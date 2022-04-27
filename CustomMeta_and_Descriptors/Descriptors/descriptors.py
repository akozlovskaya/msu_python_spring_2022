"""  Module implementing descriptors """


class Integer:
    """ Integer class """

    def __init__(self, val=None, field_name='int'):
        self.val = val
        self.field_name = field_name

    def __get__(self, obj, objtype):
        return getattr(obj, self.field_name)

    def __set__(self, obj, val):
        if isinstance(val, int):
            setattr(obj, self.field_name, val)
        else:
            raise Exception("not int")


class String:
    """ String class """

    def __init__(self, name=None, field_name='str'):
        self.name = name
        self.field_name = field_name

    def __get__(self, obj, objtype):
        return getattr(obj, self.field_name)

    def __set__(self, obj, val):
        if isinstance(val, str):
            setattr(obj, self.field_name, val)
        else:
            raise Exception("not str")


class PositiveInteger:
    """ Positive Integer class """

    def __init__(self, val=None, field_name='positive_int'):
        self.val = val
        self.field_name = field_name

    def __get__(self, obj, objtype):
        return getattr(obj, self.field_name)

    def __set__(self, obj, val):
        if isinstance(val, int) and (val > 0):
            setattr(obj, self.field_name, val)
        else:
            raise Exception("not positive int")
