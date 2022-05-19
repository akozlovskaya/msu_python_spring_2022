""" Module with tests implementation """


import unittest
import sys
import os
import io
import time
from multiprocessing import Queue, Process
from server import server
from client import client


def server_wrapper(thread_num, k, addr):
    """ Server wrapper """

    with open(os.devnull, 'w', encoding="utf8") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        server(thread_num, k, addr)
        sys.stdout = old_stdout


def client_wrapper(requests_num, urls, que, addr):
    """ Client wrapper """

    new_stdout = io.StringIO(initial_value='', newline='\n')
    old_stdout = sys.stdout
    sys.stdout = new_stdout
    client(requests_num, urls, addr)
    que.put(new_stdout.getvalue())
    sys.stdout = old_stdout
    new_stdout.close()


class FirstTestClass(unittest.TestCase):
    """ Сlient and server test class """

    def setUp(self):
        self.addr = 15000

    def tearDown(self):
        pass

    def test_ok(self):
        """ Correct URL test class """

        urls = [
                'https://en.wikipedia.org/wiki/Main_Page',
                'https://www.open.ru/',
                'https://www.msu.ru/',
                'https://cs.msu.ru/'
               ]

        queue = Queue()
        proc_1 = Process(target=server_wrapper, args=(2, 7, self.addr))
        proc_2 = Process(target=client_wrapper, args=(3, urls, queue, self.addr))

        proc_1.start()
        time.sleep(1)
        proc_2.start()

        proc_1.join()
        proc_2.join()

        answ1 = ('{"https://en.wikipedia.org/wiki/Main_Page": '
                 '{"the": 50, "of": 39, "a": 25, "in": 22, '
                 '"and": 21, "Wikipedia": 15, "that": 13}}')
        answ2 = ('{"https://www.open.ru/": '
                 '{"и": 44, "Открытие": 15, "в": 11, "на": 10, '
                 '"Банк": 9, "по": 9, "Узнать": 8}}')
        answ3 = ('{"https://www.msu.ru/": '
                 '{"и": 58, "мая": 48, "в": 47, "МГУ": 46, '
                 '"по": 38, "Универсиада": 32, "Ломоносов": 28}}')
        answ4 = ('{"https://cs.msu.ru/": '
                 '{"МГУ": 10, "по": 9, "мая": 7, "апреля": 6, '
                 '"с": 6, "ВМК": 5, "и": 5}}')

        results = sorted([s for s in queue.get().split('\n') if s])
        answers = sorted([answ1, answ2, answ3, answ4])
        self.assertEqual(results, answers)

    def test_invalid_url(self):
        """ Incorrect URL test class """

        urls = ['this_is_not_url']
        queue = Queue()
        proc_1 = Process(target=server_wrapper, args=(2, 7, self.addr + 2))
        proc_2 = Process(target=client_wrapper, args=(3, urls, queue, self.addr + 2))

        proc_1.start()
        time.sleep(1)
        proc_2.start()

        proc_1.join()
        proc_2.join()

        result = queue.get()
        while result[-1] == '\n':
            result = result[:-1]
        answer = '{"this_is_not_url": "error"}'
        self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest.main()
