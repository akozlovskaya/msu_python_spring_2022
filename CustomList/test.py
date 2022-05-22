"""  Модуль реализующий тесты для CustomList. """

import unittest

from custom_list import CustomList

def test_equal(test_class, list1, list2):
    test_class.assertEqual(len(list1), len(list2))
    for i in range(len(list1)):
        test_class.assertEqual(list1[i], list2[i])


class CustomListTestClass(unittest.TestCase):
    """  Класс реализующий тесты для CustomList. """

    def test_str(self):
        """  Метод, тестирующий строковое представление CustomList. """
        custom_list = CustomList([5, 1, 3, 7])
        self.assertEqual(str(custom_list), "items = [5, 1, 3, 7], sum = 16")

        custom_list = CustomList([5])
        self.assertEqual(str(custom_list), "items = [5], sum = 5")

        custom_list = CustomList([])
        self.assertEqual(str(custom_list), "items = [], sum = 0")

    def test_add_сustl_custl(self):
        """  Метод, тестирующий сложение CustomList и CustomList. """

        # a + b: len(a) == len(b)
        list_1 = CustomList([5, 1, 3, 7])
        list_2 = CustomList([1, 2, 7, 5])
        add_result = list_1 + list_2
        true_result = CustomList([6, 3, 10, 12])
        test_equal(self, add_result, true_result)
        test_equal(self, list_1, [5, 1, 3, 7])
        test_equal(self, list_2, [1, 2, 7, 5])
        self.assertEqual(type(add_result), CustomList)
        

        # a + b: len(a) < len(b)
        list_1 = CustomList([5, 1, 3, 7])
        list_2 = CustomList([1, 2, 7])
        add_result = CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7])
        true_result = CustomList([6, 3, 10, 7])
        test_equal(self, add_result, true_result)
        test_equal(self, list_1, [5, 1, 3, 7])
        test_equal(self, list_2, [1, 2, 7])
        self.assertEqual(type(add_result), CustomList)

        # a + b: len(a) > len(b)
        add_result = list_2 + list_1
        true_result = CustomList([6, 3, 10, 7])
        test_equal(self, add_result, true_result)
        test_equal(self, list_1, [5, 1, 3, 7])
        test_equal(self, list_2, [1, 2, 7])
        self.assertEqual(type(add_result), CustomList)
    
    def test_сustl_list(self):
        """  Метод, тестирующий сложение CustomList и List. """

        # a + b: len(a) == len(b)
        list_1 = CustomList([3, 4])
        list_2 = [1, 2]
        add_result = list_1 + list_2
        true_result = CustomList([4, 6])
        test_equal(self, add_result, true_result)
        test_equal(self, list_1, [3, 4])
        test_equal(self, list_2, [1, 2])
        self.assertEqual(type(add_result), CustomList)
        
        # a + b: len(a) < len(b)
        list_1 = CustomList([3, 4])
        list_2 = [1, 2, 5]
        add_result = list_1 + list_2
        true_result = CustomList([4, 6, 5])
        test_equal(self, add_result, true_result)
        test_equal(self, list_1, [3, 4])
        test_equal(self, list_2, [1, 2, 5])
        self.assertEqual(type(add_result), CustomList)
        
        # a + b: len(a) > len(b)
        list_1 = CustomList([3, 4])
        list_2 = [1]
        add_result = list_1 + list_2
        true_result = CustomList([4, 4])
        test_equal(self, add_result, true_result)
        test_equal(self, list_1, [3, 4])
        test_equal(self, list_2, [1])
        self.assertEqual(type(add_result), CustomList)

    def test_add_list_custl(self):
        """  Метод, тестирующий сложение List и CustomList. """

        # a + b: len(a) == len(b)
        list_1 = [5, 1, 3, 7]
        list_2 = CustomList([1, 2, 7, 5])
        add_result = list_1 + list_2
        true_result = CustomList([6, 3, 10, 12])
        test_equal(self, add_result, true_result)
        test_equal(self, list_1, [5, 1, 3, 7])
        test_equal(self, list_2, [1, 2, 7, 5])
        self.assertEqual(type(add_result), CustomList)

        # a + b: len(a) < len(b)
        list_2 = CustomList([1, 2, 7])
        add_result = list_1 + list_2
        true_result = CustomList([6, 3, 10, 7])
        test_equal(self, add_result, true_result)
        test_equal(self, list_1, [5, 1, 3, 7])
        test_equal(self, list_2, [1, 2, 7])
        self.assertEqual(type(add_result), CustomList)

        # a + b: len(a) > len(b)
        list_1 = [1, 2]
        list_2 = CustomList([3, 4, 5])
        add_result = list_1 + list_2
        true_result = CustomList([4, 6, 5])
        test_equal(self, add_result, true_result)
        test_equal(self, list_1, [1, 2])
        test_equal(self, list_2, [3, 4, 5])
        self.assertEqual(type(add_result), CustomList)

    def test_sub_сustl_custl(self):
        """  Метод, тестирующий вычитание из CustomList CustomList. """

        # a - b: len(a) == len(b)
        list_1 = CustomList([5, 1, 3, 7])
        list_2 = CustomList([1, 2, 7, 5])
        sub_result = list_1 - list_2
        true_result = CustomList([4, -1, -4, 2])
        test_equal(self, sub_result, true_result)
        test_equal(self, list_1, CustomList([5, 1, 3, 7]))
        test_equal(self, list_2, CustomList([1, 2, 7, 5]))
        self.assertEqual(type(sub_result), CustomList)

        # a - b: len(a) > len(b)
        list_1 = CustomList([5, 1, 3, 7])
        list_2 = CustomList([1, 2, 7])
        sub_result = list_1 - list_2
        true_result = CustomList([4, -1, -4, 7])
        test_equal(self, sub_result, true_result)
        test_equal(self, list_1, CustomList([5, 1, 3, 7]))
        test_equal(self, list_2, CustomList([1, 2, 7]))
        self.assertEqual(type(sub_result), CustomList)

        # a - b: len(a) < len(b)
        list_1 = CustomList([5, 1, 3])
        list_2 = CustomList([1, 2, 7, 5])
        sub_result = list_1 - list_2
        true_result = CustomList([4, -1, -4, -5])
        test_equal(self, sub_result, true_result)
        test_equal(self, list_1, CustomList([5, 1, 3]))
        test_equal(self, list_2, CustomList([1, 2, 7, 5]))
        self.assertEqual(type(sub_result), CustomList)

    def test_sub_сustl_list(self):
        """  Метод, тестирующий вычитание из CustomList List. """

        # a - b: len(a) == len(b)
        list_1 = CustomList([5, 1, 3, 7])
        list_2 = [1, 2, 7, 5]
        sub_result = list_1 - list_2
        true_result = CustomList([4, -1, -4, 2])
        test_equal(self, sub_result, true_result)
        test_equal(self, list_1, CustomList([5, 1, 3, 7]))
        test_equal(self, list_2, [1, 2, 7, 5])
        self.assertEqual(type(sub_result), CustomList)

        # a - b: len(a) > len(b)
        list_1 = CustomList([5, 1, 3, 7])
        list_2 = [1, 2, 7]
        sub_result = list_1 - list_2
        true_result = CustomList([4, -1, -4, 7])
        test_equal(self, sub_result, true_result)
        test_equal(self, list_1, CustomList([5, 1, 3, 7]))
        test_equal(self, list_2, [1, 2, 7])
        self.assertEqual(type(sub_result), CustomList)

        # a - b: len(a) < len(b)
        list_1 = CustomList([5, 1, 3])
        list_2 = [1, 2, 7, 5]
        sub_result = list_1 - list_2
        true_result = CustomList([4, -1, -4, -5])
        test_equal(self, sub_result, true_result)
        test_equal(self, list_1, CustomList([5, 1, 3]))
        test_equal(self, list_2, [1, 2, 7, 5])   
        self.assertEqual(type(sub_result), CustomList) 

    def test_sub_list_custl(self):
        """  Метод, тестирующий вычитание из List CustomList. """

        # a - b: len(a) == len(b)
        list_1 = [5, 1, 3, 7]
        list_2 = CustomList([1, 2, 7, 5])
        sub_result = list_1 - list_2
        true_result = CustomList([4, -1, -4, 2])
        test_equal(self, sub_result, true_result)
        test_equal(self, list_1, [5, 1, 3, 7])
        test_equal(self, list_2, CustomList([1, 2, 7, 5]))
        self.assertEqual(type(sub_result), CustomList)

        # a - b: len(a) > len(b)
        list_1 = [5, 1, 3, 7]
        list_2 = CustomList([1, 2, 7])
        sub_result = list_1 - list_2
        true_result = CustomList([4, -1, -4, 7])
        test_equal(self, sub_result, true_result)
        test_equal(self, list_1, [5, 1, 3, 7])
        test_equal(self, list_2, CustomList([1, 2, 7]))
        self.assertEqual(type(sub_result), CustomList)

        # a - b: len(a) < len(b)
        list_1 = [5, 1, 3]
        list_2 = CustomList([1, 2, 7, 5])
        sub_result = list_1 - list_2
        true_result = CustomList([4, -1, -4, -5])
        test_equal(self, sub_result, true_result)
        test_equal(self, list_1, [5, 1, 3])
        test_equal(self, list_2, CustomList([1, 2, 7, 5]))
        self.assertEqual(type(sub_result), CustomList)

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
