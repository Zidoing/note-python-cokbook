#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 07/12/2018.

import math


class Structure1:
    _fields = []

    def __init__(self, *args):

        if len(args) != len(self._fields):
            raise TypeError("Expected {} arguments".format(len(self._fields)))

        for name, values in zip(self._fields, args):
            setattr(self, name, values)


class Stock(Structure1):
    _fields = ["name", "share", "price"]


class Point(Structure1):
    _fields = ["x", "y"]


class Circle(Structure1):
    _fields = ["raidus"]

    def area(self):
        return math.pi * self.raidus ** 2
