#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-18.


def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.sahres * self.price


cls_dict = {
    '__init__': __init__,
    "cost": cost
}

import types

Stock = types.new_class("Stock", (), {}, lambda ns: ns.update(cls_dict))

print(Stock.__module__)

Stock.__module__ = __name__

print(Stock.__module__)

s = Stock(1, 2, 2)
