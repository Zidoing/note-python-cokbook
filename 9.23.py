#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-18.


a = 13

exec("b = a +1")

print(b)






def test2():

    x = 0

    loc = locals()
    print(locals())

    exec("x += 1")
    print(loc)
    print(loc['loc'])
    print(loc['x'])
    print(x)



test2()