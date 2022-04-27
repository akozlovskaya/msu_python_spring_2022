"""  Module implementing CustomMeta tests """

import unittest

from custom_meta import CustomMeta


class CustomClass(metaclass=CustomMeta):
    """ Class to test CustomMeta """
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        """ return 100 """
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


class CustomMetaTestClass(unittest.TestCase):
    """ Class implementing CustomMeta tests """

    def test_correct(self):
        """ Testing correct use of CustomClass """
        inst = CustomClass()
        self.assertEqual(inst.custom_x, 50)
        self.assertEqual(inst.custom_val, 99)
        self.assertEqual(inst.custom_line(), 100)
        self.assertEqual(CustomClass.custom_x, 50)
        self.assertEqual(str(inst), "Custom_by_metaclass")

        inst.dynamic = "added later"
        self.assertEqual(inst.custom_dynamic, "added later")

    def test_incorrect(self):
        """ Testing incorrect use of CustomClass """
        inst = CustomClass()
        with self.assertRaises(AttributeError):
            print(inst.x)
        with self.assertRaises(AttributeError):
            print(inst.val)
        with self.assertRaises(AttributeError):
            print(inst.line())
        with self.assertRaises(AttributeError):
            print(inst.yyy)
        with self.assertRaises(AttributeError):
            print(CustomClass.x)


if __name__ == '__main__':
    unittest.main()
