#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-18.


class NoMixedCaseMeta(type):

    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError("bad attribute name: " + name)

        print(clsname)
        print(bases)
        print(clsdict)
        return super(NoMixedCaseMeta, cls).__new__(cls, clsname, bases, clsdict)


class Root(metaclass=NoMixedCaseMeta):
    pass


class A(Root):
    def foo_bar(self, a, b):
        pass



print(getattr(A, 'foo_bar'))


from inspect import signature


print(signature(getattr(A, 'foo_bar')))