"""  Модуль реализующий LRUCache """


class LRUCache:
    """  Кэш с вытеснием неиспользованных дольше всех значений """

    def __init__(self, limit=42):
        if not isinstance(limit, int) or limit <= 0:
            raise Exception("LRUCache: bad limit")
        self.data = {}
        self.limit = limit
        self.keys = []

    def get(self, key):
        """ Получение элемента из кэша по ключу """
        if key not in self.data:
            return None
        self.keys.remove(key)
        self.keys.append(key)
        return self.data[key]

    def set(self, key, value):
        """ Сохранение элемента в кэш по ключу """
        if key in self.data:
            self.keys.remove(key)
        elif len(self.keys) == self.limit:
            deleted = self.keys.pop(0)
            del self.data[deleted]
        self.keys.append(key)
        self.data[key] = value
