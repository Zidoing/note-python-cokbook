#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 14/11/2018.
a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

print(a.keys() & b.keys())

print(a.keys() - b.keys())

print(a.items() & b.items())

c = {key: a[key] for key in a.keys() - {'z', 'w'}}
