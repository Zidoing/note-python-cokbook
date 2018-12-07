#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 07/12/2018.


class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

##  slot 的主要目的是内存优化  而非 禁止 用户自己添加属性和


