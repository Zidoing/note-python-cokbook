#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 07/12/2018.


class A:

    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        pass

    def _internal_method(self):
        pass


class B:

    def __init__(self):
        self.__private = 0

    def __private_method(self):
        pass

    def public_method(self):
        pass

        self.__private_method()


print(B()._B__private)
