#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 10/12/2018.


import time


class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


a = Date(2012, 12, 21)

b = Date.today()
