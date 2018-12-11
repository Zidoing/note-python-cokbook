#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 10/12/2018.


class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B1:

    def __init__(self):
        self._a = A()

    def spam(self, x):
        return self._a.spam(x)

    def foo(self):
        return self._a.foo()

    def bar(self):
        pass


class B2:

    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    def __getattr__(self, item):
        return getattr(self._a, item)


b = B1()

b.bar()
b.spam(1)
