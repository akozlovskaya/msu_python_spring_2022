"""  Модуль, реализующий тесты для CustomList. """

import unittest

from custom_list import CustomList


class CustomListTestClass(unittest.TestCase):
    """  Класс, реализующий тесты для CustomList. """

    def test_str(self):
        """  Метод, тестирующий строковое представление CustomList. """
        custom_list = CustomList([5, 1, 3, 7])
        self.assertEqual(str(custom_list), "items = [5, 1, 3, 7], sum = 16")

        custom_list = CustomList([5])
        self.assertEqual(str(custom_list), "items = [5], sum = 5")

        custom_list = CustomList([])
        self.assertEqual(str(custom_list), "items = [], sum = 0")

    # так как сравнение списков перегружено, далее будем использовать
    # сравнение str(CustomList), убедившись в корректной работе этого метода
    def test_add(self):
        """  Метод, тестирующий сложение CustomList и CustomList/list. """
        add_result = CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7])
        true_result = CustomList([6, 3, 10, 7])
        self.assertEqual(str(add_result), str(true_result))

        add_result = [1, 2] + CustomList([3, 4])
        true_result = CustomList([4, 6])
        self.assertEqual(str(add_result), str(true_result))

        add_result = CustomList([3, 4]) + [1, 2]
        true_result = CustomList([4, 6])
        self.assertEqual(str(add_result), str(true_result))

    def test_sub(self):
        """  Метод, тестирующий вычитание CustomList и CustomList/list. """
        add_result = CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7])
        true_result = CustomList([4, -1, -4, 7])
        self.assertEqual(str(add_result), str(true_result))

        add_result = [1, 2] - CustomList([3, 4])
        true_result = CustomList([-2, -2])
        self.assertEqual(str(add_result), str(true_result))

        add_result = CustomList([3, 4]) - [1, 2]
        true_result = CustomList([2, 2])
        self.assertEqual(str(add_result), str(true_result))

    def test_comparison(self):
        """  Метод, тестирующий сравнение CustomList. """
        list_sum_16 = CustomList([5, 1, 3, 7])
        list_sum_16_ = CustomList([1, 8, 7])
        list_sum_8 = CustomList([1, 7])

        self.assertTrue(list_sum_16 == list_sum_16_)
        self.assertFalse(list_sum_16 == list_sum_8)

        self.assertTrue(list_sum_16 != list_sum_8)
        self.assertFalse(list_sum_16 != list_sum_16_)

        self.assertFalse(list_sum_8 > list_sum_16)
        self.assertTrue(list_sum_16 >= list_sum_16_)
        self.assertFalse(list_sum_16 <= list_sum_8)
        self.assertFalse(list_sum_16 < list_sum_16_)


if __name__ == '__main__':
    unittest.main()
