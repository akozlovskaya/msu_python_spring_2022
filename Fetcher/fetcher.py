""" Script to process list of urls """


import asyncio
import sys
import aiohttp


async def fetch_proc_url(name, session, url_queue):
    """ Function that processes the url from the queue """

    while True:
        url = await url_queue.get()
        try:
            async with session.get(url, timeout=2) as resp:
                data = await resp.read()
                print("name", name, len(data))
        except asyncio.TimeoutError:
            print('Timeout')
        except aiohttp.ServerDisconnectedError:
            print('Server Disconnected')
        finally:
            url_queue.task_done()


async def fetch_make_queue(file, url_queue):
    """ Function that receives urls from file and makes queues """

    for line in file:
        url = line.rstrip('\n')
        await url_queue.put(url)


async def crawl(filename, threads=5, qsize=20):
    """ Function that concurrently processing urls from file """

    queue = asyncio.Queue(maxsize=qsize)
    file = open(filename, 'r', encoding="utf8")
    async with aiohttp.ClientSession() as session:
        task_queue = asyncio.create_task(fetch_make_queue(file, queue))
        tasks = [
            asyncio.create_task(fetch_proc_url(f"coro_{i}", session, queue))
            for i in range(threads)
        ]
        await task_queue
        await queue.join()
    for task in tasks:
        task.cancel()
    task_queue.cancel()
    file.close()


async def main():
    """ Main function """
    await crawl(fname, th_num)

if __name__ == "__main__":

    i = 0
    if '-c' in sys.argv:
        i = sys.argv.index('-c')
    th_num = int(sys.argv[i + 1])
    fname = sys.argv[i + 2]

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
