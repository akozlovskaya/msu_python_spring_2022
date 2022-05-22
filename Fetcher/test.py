""" Test module """


import os
import sys
import asyncio
import time
from aiohttp.test_utils import AioHTTPTestCase

from fetcher import crawl


class MyAppTestCase(AioHTTPTestCase):
    """ Test class """

    async def test_1(self):
        """ Time test """
        self.devnull = open(os.devnull, "w", encoding="utf8")
        self.old_stdout = sys.stdout
        sys.stdout = self.devnull

        counter_1 = time.perf_counter()
        await crawl(threads=5, filename='urls1.txt', qsize=5)
        counter_2 = time.perf_counter()
        time_1 = counter_2 - counter_1

        counter_1 = time.perf_counter()
        await crawl(threads=20, filename='urls1.txt', qsize=5)
        counter_2 = time.perf_counter()
        time_2 = counter_2 - counter_1

        counter_1 = time.perf_counter()
        await crawl(threads=20, filename='urls1.txt', qsize=0)
        counter_2 = time.perf_counter()
        time_3 = counter_2 - counter_1

        sys.stdout = self.old_stdout
        self.devnull.close()

        self.assertTrue(time_1 > time_2)
        self.assertTrue(time_2 > time_3)


if __name__ == '__main__':
    my_test = MyAppTestCase()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(my_test.test_1())
