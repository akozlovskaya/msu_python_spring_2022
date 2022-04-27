"""  Module implementing descriptors tests """

import unittest

from descriptors import Integer, String, PositiveInteger


class Data:
    """ Class to test descriptors """
    num = Integer()
    name = String()
    price = PositiveInteger()

    def __init__(self, num=-1, name='Name', price=100):
        self.num = num
        self.name = name
        self.price = price


class DescriptorsTestClass(unittest.TestCase):
    """ Descriptors tests class """

    def test_correct(self):
        """ Testing correct use of descriptors """
        my_data = Data()
        self.assertEqual(my_data.num, -1)
        self.assertEqual(my_data.name, 'Name')
        self.assertEqual(my_data.price, 100)
        my_data.num = 15
        my_data.price = 10
        my_data.name = '^_^'
        self.assertEqual(my_data.num, 15)
        self.assertEqual(my_data.name, '^_^')
        self.assertEqual(my_data.price, 10)

        correct_dict = {'int': 15, 'str': '^_^', 'positive_int': 10}
        self.assertEqual(my_data.__dict__, correct_dict)

        my_data.num = -100
        correct_dict['int'] = -100
        self.assertEqual(my_data.__dict__, correct_dict)

    def test_incorrect(self):
        """ Testing incorrect use of descriptors """
        my_data = Data()
        with self.assertRaises(Exception):
            my_data.num = 1.5
        with self.assertRaises(Exception):
            my_data.num = 'aaa'
        with self.assertRaises(Exception):
            my_data.name = 38
        with self.assertRaises(Exception):
            my_data.price = -1
        with self.assertRaises(Exception):
            my_data.price = 100.5


if __name__ == '__main__':
    unittest.main()
