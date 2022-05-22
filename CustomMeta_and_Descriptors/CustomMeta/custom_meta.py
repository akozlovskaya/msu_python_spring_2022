""" Module implementing metaclass """


class CustomMeta(type):
    """ Metaclass that adds the prefix 'custom_' to the beginning
    of the names of all attributes and methods (except magic ones) """

    def __new__(cls, name, parents, attr):
        """ Called to create a new instance of class """
        magic_methods = dict((name, val) for name, val in attr.items()
                             if name.startswith('__') and name.endswith('__'))
        custom = dict(('custom_' + name, val) for name, val in attr.items()
                      if not name.startswith('__'))
        new_attrs = {**custom, **magic_methods}
        old_set_attr = object.__setattr__
        new_attrs['old_set_attr'] = old_set_attr

        def set_custom_attr(self, name, value):
            """ Called when an attribute assignment is attempted """
            new_name = name
            if not name.startswith('__'):
                new_name = 'custom_' + name
            self.old_set_attr(new_name, value)

        new_attrs['__setattr__'] = set_custom_attr

        return super(CustomMeta, cls).__new__(cls, name, parents, new_attrs)
