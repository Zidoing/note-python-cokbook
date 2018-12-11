#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 11/12/2018.


import types
from functools import wraps


class Profiled:

    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1

        print(self.__wrapped__)
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@Profiled
def add(x, y):
    return x + y


print(add(3, 3))