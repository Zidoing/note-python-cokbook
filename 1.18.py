#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 16/11/2018.
from collections import namedtuple

Subscriber = namedtuple("Subscriber", ["addr", "joined"])

sub = Subscriber("jonesy@example.com", '2012-10-19')

print(sub)

print(sub.addr)

print(sub.joined)

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

stock_prototype = Stock('', 0, 0.0, None, None)


def dict_to_stock(s):
    return stock_prototype._replace(**s)


