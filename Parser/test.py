import unittest
from unittest.mock import Mock
from faker import Faker
import sys
import os
from Parser import parse_html


class RandomHTMLFactory:
    fake = Faker()

    def html_str(self):
        class_atr = self.fake.word()
        src_atr = self.fake.word()+'.png'
        href = f'{self.fake.word()}://{self.fake.word()}/{self.fake.word()}/'
        data = self.fake.texts(nb_texts=5, max_nb_chars=20)
        ret = f'<html>{data[0]}<body class={class_atr}>{data[1]}'\
            + f'<p src={src_atr} href="{href}">{data[2]}'\
            + f'</p>{data[3]}</body>{data[4]}</html>'
        return ret

    def bad_html(self, num):
        if num % 2:
            return f'<html>{self.fake.text(max_nb_chars=50)}</html'
        else:
            return '<html>'+self.fake.text(max_nb_chars=50)


def fun1(str, attributes):
    print('open tag:', str)
    for key in attributes:
        print('\t', key, '=', attributes[key])


def fun2(str):
    print('data:', str)


def fun3(str):
    print('close tag:', str)


class FirstTestClass(unittest.TestCase):

    factory = RandomHTMLFactory()

    def setUp(self):
        self.devnull = open(os.devnull, "w")
        self.old_stdout = sys.stdout
        sys.stdout = self.devnull

    def tearDown(self):
        sys.stdout = self.old_stdout
        self.devnull.close()

    def test_mock(self):
        mock_1 = Mock()
        mock_2 = Mock()
        mock_3 = Mock()
        html_str = self.factory.html_str()
        parse_html(html_str, mock_1, mock_2, mock_3)
        self.assertEqual(mock_1.call_count, 3)
        self.assertEqual(mock_2.call_count, 5)
        self.assertEqual(mock_3.call_count, 3)

    def test_invalid_string(self):
        with self.assertRaises(Exception, msg='Error: Invalid html string'):
            parse_html(self.factory.bad_html(0))
        with self.assertRaises(Exception, msg='Error: Invalid html string'):
            parse_html(self.factory.bad_html(1))


if __name__ == '__main__':
    unittest.main()
