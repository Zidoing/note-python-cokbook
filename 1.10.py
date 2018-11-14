#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 14/11/2018.


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 2, 3, 4, 5, 6, 7, 7, 1, 10]

print(list(dedupe(a)))


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
