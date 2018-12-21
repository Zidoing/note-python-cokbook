#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-21.


from socket import AF_INET, SOCK_STREAM, socket

from concurrent.futures import ThreadPoolExecutor


def echo_client(sock, client_addr):
    print("got connection ", client_addr)

    while True:

        msg = sock.recv(65526)

        if not msg:
            break

        sock.sendall(msg)

    print("client closed connection")

    sock.close()


def echo_server(addr):
    pool = ThreadPoolExecutor(128)

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)

    sock.listen(5)

    while True:
        client_sock, client_addr = sock.accept()

        pool.submit(echo_client, client_sock, client_addr)




echo_server(('',15000))
