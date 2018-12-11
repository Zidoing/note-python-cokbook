#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 10/12/2018.


import logging

a = logging.getLogger("foo")

b = logging.getLogger("bar")

print(a is b)

c = logging.getLogger("foo")

print(a is c)


class Spam:
    def __init__(self, name):
        self.name = name


import weakref

_spam_cache = weakref.WeakValueDictionary()


def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]

    return s


a = get_spam("davie")
b = get_spam("davie")

print(a is b)


class Spam:
    _spam_cache = weakref.WeakValueDictionary()

    def __new__(cls, name, *args, **kwargs):
        print(name, args, kwargs)
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self

            return self

    def __init__(self, name, *args, **kwargs):
        print("initializing spam")

        self.name = name


a = Spam(1, 2, 3, df=2)
b = Spam(1, 2, 3, df=2)
