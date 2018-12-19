#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-18.


def countdown(n):
    while n > 0:
        print("T-minus", n)
        n -= 1

    print("blastoff")


import dis

dis.dis(countdown)

print(countdown.__code__.co_code)
