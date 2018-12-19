#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-18.


class Spam:

    def __init__(self, name):
        self.name = name


a = Spam("Guido")
b = Spam("Diana")


class NoInstances(type):

    def __call__(self, *args, **kwargs):
        raise TypeError("can not instaniate directly")


class Spam(metaclass=NoInstances):

    @staticmethod
    def grok(x):
        print("spam.grok")


class Singleton(type):

    def __init__(self, *args, **kwargs):
        self.__instance = None
        super(Singleton, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super(Singleton, self).__call__(*args, **kwargs)

        return self.__instance


class Spam2(metaclass=Singleton):

    def __init__(self):
        print("create spam")


a = Spam2()
b = Spam2()
print(a is b)

print(a.__class__)
print(a.__class__.__bases__)

import weakref


class Cached(type):

    def __init__(self, *args, **kwargs):
        super(Cached, self).__init__(*args, **kwargs)
        print(self)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args, **kwargs):

        if args in self.__cache:
            return self.__cache[args]

        else:
            obj = super(Cached, self).__call__(*args, **kwargs)
            self.__cache[args] = obj
            return obj



class K(Cached):
    pass


