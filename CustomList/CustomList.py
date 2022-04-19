class CustomList(list):
    def __init__(self, src):
        super().__init__(src)

    def __add__(self, other):
        ret = CustomList([a+b for a, b in zip(self, other)])
        if len(other) > len(self):
            ret += other[len(self):]
        if len(other) < len(self):
            ret += self[len(other):]
        return ret

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        ret = CustomList([a-b for a, b in zip(self, other)])
        if len(other) > len(self):
            ret += [-i for i in other[len(self):]]
        if len(other) < len(self):
            ret += self[len(other):]
        return ret

    def __rsub__(self, other):
        return CustomList([-i for i in self - other])

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __str__(self):
        items = ', '.join([str(i) for i in self])
        return 'items = [{}], sum = {}'.format(items, sum(self))
