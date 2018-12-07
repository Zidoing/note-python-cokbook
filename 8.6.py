#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 07/12/2018.


class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")

        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")





p = Person("zhoulei")



print(p.first_name)
