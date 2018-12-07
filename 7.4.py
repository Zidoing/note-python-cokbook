#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 06/12/2018.


def myfun():
    return 1, 2, 3


a, b, c = myfun()


def spam(a, b=43):
    print(a, b)


spam(1, 2)
spam(1)
spam(1, None)
