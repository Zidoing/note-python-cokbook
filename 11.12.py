# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-20.


class EventHandler:

    def fileno(self):
        raise NotImplementedError

    def wants_to_receive(self):
        return False

    def handle_receive(self):
        pass

    def wants_to_send(self):
        return False

    def handle_send(self):
        pass


import select


def event_loop(handlers):
    while True:
        wants_recv = [h for h in handlers if h.wants_to_receive()]
        wants_send = [h for h in handlers if h.wants_to_send()]

        can_recv, can_send, _ = select.select(wants_recv, wants_send, [])

        for h in can_recv:
            h.handle_receive()

        for h in can_send:
            h.handle_send()
