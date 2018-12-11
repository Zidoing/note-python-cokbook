# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 11/12/2018.


import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        r = func(*args, **kwargs)

        end = time.time()

        print(end - start)

        return r

    return wrapper


class Spam:

    @timethis
    def instance_method(self, n):
        print(self, n)

        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1
