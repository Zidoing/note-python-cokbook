#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-20.


from socket import socket, AF_INET, SOCK_STREAM

import ssl


def echo_client(s):
    while True:

        data = s.recv(8192)
        if data == b"":
            break

        s.send(data)

    s.close()

    print("connection closed")


def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)

    s.bind(address)
    s.listen(1)

    s_ssl = ssl.wrap_socket(s, )
