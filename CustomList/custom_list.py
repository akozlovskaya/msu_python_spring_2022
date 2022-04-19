"""  Модуль, реализующий пользовательский список. """


class CustomList(list):
    """  Класс, реализующий пользовательский список. """

    def __add__(self, other):
        """ Метод, реализующий левое сложение. """
        ret = CustomList([a+b for a, b in zip(self, other)])
        if len(other) > len(self):
            ret += other[len(self):]
        if len(other) < len(self):
            ret += self[len(other):]
        return ret

    def __radd__(self, other):
        """ Метод, реализующий правое сложение. """
        return self + other

    def __sub__(self, other):
        """ Метод, реализующий левое вычитание. """
        ret = CustomList([a-b for a, b in zip(self, other)])
        if len(other) > len(self):
            ret += [-i for i in other[len(self):]]
        if len(other) < len(self):
            ret += self[len(other):]
        return ret

    def __rsub__(self, other):
        """ Метод, реализующий правое вычитание. """
        return CustomList([-i for i in self - other])

    def __eq__(self, other):
        """ Метод, реализующий оператор равенства. """
        return sum(self) == sum(other)

    def __ne__(self, other):
        """ Метод, реализующий оператор неравенства. """
        return sum(self) != sum(other)

    def __lt__(self, other):
        """ Метод, реализующий оператор «меньше». """
        return sum(self) < sum(other)

    def __le__(self, other):
        """ Метод, реализующий оператор «меньше или равно». """
        return sum(self) <= sum(other)

    def __gt__(self, other):
        """ Метод, реализующий оператор «больше». """
        return sum(self) > sum(other)

    def __ge__(self, other):
        """ Метод, реализующий оператор «больше или равно». """
        return sum(self) >= sum(other)

    def __str__(self):
        """ Метод, реализующий строковое представление CustomList. """
        items = ', '.join([str(i) for i in self])
        return f'items = [{items}], sum = {sum(self)}'
