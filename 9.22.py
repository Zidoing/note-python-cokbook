#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-18.


import time

from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()

    try:
        print("1")
        yield
        print("2")

    finally:
        end = time.time()
        print(f'{label}:{end - start}')


with timethis("counting") as f:
    n = 10000000
    while n > 0:
        n -= 1


@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)

    yield working

    orig_list[:] = working


items = [1, 2, 3]

with list_transaction(items) as working:
    working.append(4)
    working.append(5)

print(items)
