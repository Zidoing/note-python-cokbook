#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-18.


import operator


class StructTupleMeta(type):

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))


class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []

    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError('{} arguments required'.format(len(cls._fields)))
        return super().__new__(cls, args)


class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']


class Point(StructTuple):
    _fields = ['x', 'y']

s = Stock('ACME', 50, 91.1)
