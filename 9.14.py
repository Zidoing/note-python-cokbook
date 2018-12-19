#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-18.
from collections import OrderedDict


class Typed:
    _expected_type = type(None)

    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        if not instance(value, self._expected_type):
            raise TypeError("expected " + str(self._expected_type))

        instance.__dict__[self._name] = value


class Integer(Typed):
    _expected_type = int


class Fload(Typed):
    _expected_type = float


class String(Typed):
    _expected_type = str


class OrderdMeta(type):

    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)

        order = []
        for name, value in clsdict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)

        d["_order"] = order

        return type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(mcs, name, bases):
        return OrderedDict()
