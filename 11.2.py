#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-19.
import time
from socketserver import BaseRequestHandler, TCPServer, UDPServer


class EchoHandler(BaseRequestHandler):

    def handle(self):

        print(f"Got connection from {self.client_address}")

        while True:

            msg = self.request.recv(8192)

            if not msg:
                print("break")
                break

            self.request.send(msg)


class TimeHandler(BaseRequestHandler):

    def handle(self):
        print(f"got connect from {self.client_address}")

        msg, sock = self.request

        resp = time.ctime()

        sock.sendto(resp.encode("ascii"), self.client_address)


if __name__ == '__main__':
    # serv = TCPServer(("", 20000), EchoHandler)
    serv = UDPServer(("", 20000), TimeHandler)
    serv.serve_forever()
