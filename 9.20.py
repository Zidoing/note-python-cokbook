#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-18.
class Spam:
    def bar(self, x: int, y: int):
        print('Bar 1:', x, y)

    def bar(self, s: str, n: int = 0):
        print('Bar 2:', s, n)


s = Spam()
s.bar(2, 3)  # Prints Bar 1: 2 3
s.bar('hello')  # Prints Bar 2: hello 0
