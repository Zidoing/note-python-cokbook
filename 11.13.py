#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-21.


def send_from(arr, dest):
    view = memoryview(arr).cast("B")

    while len(view):
        nsent = dest.send(view)

        view = view[nsent:]


def recv_into(arr, source):
    view = memoryview(arr).cast("B")

    while len(view):
        nrecv = source.recv_into(view)

        view = view[nrecv:]
