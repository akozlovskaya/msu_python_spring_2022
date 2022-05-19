""" Module with client implementation """


import socket
import sys
from threading import Thread
from queue import Queue


def client_connect(addr1, addr2):
    """ Connect to the server """

    sock = socket.socket()
    sock1 = socket.socket()

    sock.connect(("", addr1))
    sock1.connect(("", addr2))
    return sock, sock1


def proc_url(queue, sock, sock1):
    """ URL  processing """

    while not queue.empty():
        url = queue.get()
        sock.sendall(url.encode('utf-8'))
        data = sock1.recv(1024).decode('utf-8')
        print(data)


def make_urls_list(filename):
    """ URL list formation """

    with open(filename, 'r', encoding="utf8") as file:
        urls_list = file.readlines()
    return urls_list


def client(thread_num, urls, addr=15000):
    """ Client """

    sock, sock1 = client_connect(addr, addr + 1)

    queue = Queue()
    for url in urls:
        if url[-1] != '\n':
            queue.put(url + '\n')
        else:
            queue.put(url)
    queue.put('STOP')

    threads = [
        Thread(target=proc_url, args=(queue, sock, sock1))
        for i in range(thread_num)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    sock.close()
    sock1.close()


if __name__ == "__main__":

    thread_number = int(sys.argv[1])
    name = sys.argv[2]
    url_list = make_urls_list(name)
    client(thread_number, url_list)
