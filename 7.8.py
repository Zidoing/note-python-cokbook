#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 06/12/2018.


def spam(a, b, c, d):
    print(a, b, c, d, )


from functools import partial

s1 = partial(spam, 1)


