#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 11/12/2018.


from functools import wraps


class A:

    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("decorate 1")
            return func(*args, **kwargs)

        return wrapper

    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("decorate 2")
            return func(*args, **kwargs)

        return wrapper


a = A()


@a.decorator1
def spam():
    pass


@A.decorator2
def grok():
    pass


spam()

grok()
