"""  Модуль реализующий тесты для LRUCache """

import unittest

from lru_cache import LRUCache


class LRUCacheTestClass(unittest.TestCase):
    """  Класс, реализующий тесты для LRUCache """

    def test_cache(self):
        """  Метод, тестирующий работу LRUCache """

        cache_2 = LRUCache(2)

        cache_2.set("k1", "val1")
        cache_2.set("k2", "val2")

        self.assertEqual(cache_2.get("k3"), None)
        self.assertEqual(cache_2.get("k2"), "val2")
        self.assertEqual(cache_2.get("k1"), "val1")

        cache_2.set("k3", "val3")

        self.assertEqual(cache_2.get("k3"), "val3")
        self.assertEqual(cache_2.get("k2"), None)
        self.assertEqual(cache_2.get("k1"), "val1")

    def test_types(self):
        """  Метод, тестирующий работу LRUCache с различными типами """

        cache_3 = LRUCache(3)
        cache_3.set(15, "val_15")
        cache_3.set("key", "val_key")
        cache_3.set("list_key", [1, 2])

        self.assertEqual(cache_3.get(15), "val_15")
        self.assertEqual(cache_3.get("key"), "val_key")
        self.assertEqual(cache_3.get("list_key"), [1, 2])

        cache_3.set(16, "val_16")
        self.assertEqual(cache_3.get(15), None)

    def test_size_1(self):
        """  Метод, тестирующий работу LRUCache размера 1"""

        cache_1 = LRUCache(1)
        cache_1.set("key", "val")
        self.assertEqual(cache_1.get("key"), "val")
        cache_1.set("new_key", "new_val")
        self.assertEqual(cache_1.get("key"), None)
        self.assertEqual(cache_1.get("new_key"), "new_val")

    def test_init(self):
        """  Метод, тестирующий некорректное создание LRUCache """

        with self.assertRaises(Exception):
            bad_cache = LRUCache(0)
        with self.assertRaises(Exception):
            bad_cache = LRUCache(-5)
        with self.assertRaises(Exception):
            bad_cache = LRUCache(0.3)
        with self.assertRaises(Exception):
            bad_cache = LRUCache('name')

     def test_displacement(self):
        """  Метод, тестирующий работу LRUCache с полным вытеснением """

        cashe = LRUCache(2)
        cashe.set("key_1", "val_1")
        cashe.set("key_2", "val_2")
        cashe.set("key_3", "val_3")
        cashe.set("key_4", "val_4")
        self.assertEqual(cashe.get("key_1"), None)
        self.assertEqual(cashe.get("key_2"), None)
        self.assertEqual(cashe.get("key_3"), "val_3")
        self.assertEqual(cashe.get("key_4"), "val_4")

     def test_new_value(self):
        """  Метод, тестирующий работу LRUCache
        set нового значения существующему ключу key_2:
        этот ключ теперь удалится в последнюю очередь """

        cashe = LRUCache(3)
        cashe.set("key_1", "val_1")
        cashe.set("key_2", "val_2")
        cashe.set("key_3", "val_3")
        cashe.set("key_2", "new_value")
        cashe.set("new_key_a", "val_a")
        cashe.set("new_key_b", "val_b")
        self.assertEqual(cashe.get("key_1"), None)
        self.assertEqual(cashe.get("key_3"), None)
        self.assertEqual(cashe.get("key_2"), "new_value")


if __name__ == '__main__':
    unittest.main()
