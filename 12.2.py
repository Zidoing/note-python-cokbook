#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-21.


from threading import Thread, Event

import time


def countdown(n, start_evt):
    print("countdown starting")

    start_evt.set()

    while n > 0:
        print("T - minus", n)

        n -= 1
        time.sleep(5)


start_evt = Event()

print("launching count down")

t = Thread(target=countdown, args=(10, start_evt))
t.start()



start_evt.wait()

print("countdown is running")