#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 10/12/2018.


import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


p = Point(2, 3)

d = getattr(p, 'distance')(0, 0)

print(d)

import operator

print(operator.methodcaller("distance", 0, 0)(p))