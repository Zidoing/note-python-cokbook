#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 10/12/2018.


class Descriptor:

    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Stock:
    descriptor = Descriptor()


a = Stock()
print(a)
a.descriptor = 2
print(a.descriptor)


class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not instance(value, self.expected_type):
            raise TypeError("expected" + str(self.expected_type))
        super().__set__(instance, value)


class Unsigned(Descriptor):

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("expected >= 0 ")
        super().__set__(instance, value)


class MaxSized(Descriptor):

    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError("missing size option")

        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            super().__set__(instance, value)


def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)

            else:
                setattr(cls, key, value(key))

        return cls

    return decorate
