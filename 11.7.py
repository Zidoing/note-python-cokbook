#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-19.


from multiprocessing.connection import Listener

import traceback


def echo_client(conn):
    try:
        while True:
            msg = conn.rece()
            conn.send(msg)

    except EOFError:

        print("connection closed")


def echo_server(address, authkey):
    serv = Listener(address, authkey=authkey)

    while True:
        try:
            client = serv.accept()

            echo_client(client)

        except Exception:
            traceback.print_exc()
