""" Module with server implementation """


import socket
import sys

from threading import Thread, Lock
from queue import Queue

import re
import json
import requests
from bs4 import BeautifulSoup


def serv_connect(addr1, addr2):
    """ Connect to the client """

    sock = socket.socket()
    sock.bind(("", addr1))
    sock.listen(5)

    sock1 = socket.socket()
    sock1.bind(("", addr2))
    sock1.listen(5)

    client = sock.accept()[0]
    client1 = sock1.accept()[0]

    return client, client1, sock, sock1


def process_url(queue, num, lock, client, k):
    """ Worker: URL  processing """

    while True:
        url = queue.get()
        if url == 'STOP':
            queue.put(url)
            break
        try:
            req = requests.get(url, timeout=3)
        except requests.ConnectionError:
            res_json = json.dumps({url: 'error'}, ensure_ascii=False)
        except requests.exceptions.MissingSchema:
            res_json = json.dumps({url: 'error'}, ensure_ascii=False)
        except requests.exceptions.ReadTimeout:
            res_json = json.dumps({url: 'error'}, ensure_ascii=False)
        else:
            soup = BeautifulSoup(req.text, features="html.parser")
            words = re.findall(r'[a-zA-Zа-яёА-ЯЁ_]+', soup.text)
            unique = dict(zip(words, [words.count(i) for i in words]))
            res = sorted(unique.items(), key=lambda x: -x[1])[:k]
            res_dict = {url: {item[0]: item[1] for item in res}}
            res_json = json.dumps(res_dict, ensure_ascii=False)
        client.send(res_json.encode('utf-8'))
        with lock:
            num[0] += 1
            print(num[0], 'urls processed')


def get_url(queue, client):
    """ Master: URL queue formation """

    while True:
        urls = client.recv(4096).decode('utf-8').split('\n')
        for url in urls:
            if url:
                queue.put(url)
            if url == 'STOP':
                return


def server(workers_number, k, addr=15000):
    """ Server """

    client, client1, sock, sock1 = serv_connect(addr, addr + 1)

    lock = Lock()
    queue = Queue()
    num = [0]

    threads = [
        Thread(target=process_url, args=(queue, num, lock, client1, k))
        for i in range(workers_number + 1)
    ]
    threads.append(Thread(target=get_url, args=(queue, client)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    sock.close()
    sock1.close()


if __name__ == "__main__":

    N = int(sys.argv[2])
    K = int(sys.argv[4])
    server(N, K)
