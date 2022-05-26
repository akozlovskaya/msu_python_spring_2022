"""  Модуль реализующий LRUCache с логгированием """


import sys
import logging


class LRUCache:
    """  Кэш с вытеснием неиспользованных дольше всех значений """

    def __init__(self, limit=42, stream_log=False):
        handlers = [logging.FileHandler(filename='tmp.log')]
        if stream_log:
            handlers.append(logging.StreamHandler(sys.stdout))

        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s\t%(levelname)s\t%(message)s',
            handlers=handlers
        )
        self.logger = logging.getLogger()
        if not isinstance(limit, int) or limit <= 0:
            self.logger.error("bad limit")
            raise Exception("LRUCache: bad limit")
        self.data = {}
        self.limit = limit
        self.keys = []
        self.logger.debug("LRUCache created")

    def get(self, key):
        """ Получение элемента из кэша по ключу """
        if key not in self.data:
            self.logger.warning("get: key %s not in cache", key)
            return None
        self.keys.remove(key)
        self.keys.append(key)
        return self.data[key]

    def set(self, key, value):
        """ Сохранение элемента в кэш по ключу """
        if key in self.data:
            self.keys.remove(key)
            self.logger.debug("set: key %s removed", key)
        elif len(self.keys) == self.limit:
            deleted = self.keys.pop(0)
            del self.data[deleted]
            self.logger.debug("set: key %s deleted", key)
        self.keys.append(key)
        self.data[key] = value
        self.logger.debug("set: %s -> %s created", key, value)


if __name__ == "__main__":
    STREAM_LOG = '-s' in sys.argv
    # Error:
    # cache = LRUCache(-5, STREAM_LOG)
    cache = LRUCache(2, STREAM_LOG)
    cache.set("key_1", "val_1")
    cache.set("key_2", "val_2")
    cache.set("key_3", "val_3")
    cache.set("key_4", "val_4")
    val = cache.get("key_1")
    val = cache.get("key_3")
