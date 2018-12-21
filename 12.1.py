#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-21.


import time


def countdown(n):
    while n > 0:
        print("T-minus", n)

        n -= 1

        time.sleep(5)


from threading import Thread

t = Thread(target=countdown, args=(10,), daemon=True)


t.start()
t.join()