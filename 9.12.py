#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 11/12/2018.


def log_getattribute(cls):
    orig_getattribute = cls.__getattribute__

    def new_getattribute(self, name):
        print("getting: ", name)

        return orig_getattribute(self, name)

    cls.__getattribute__ = new_getattribute

    return cls


@log_getattribute
class A:
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass


a = A(42)

a.x

a.spam()
