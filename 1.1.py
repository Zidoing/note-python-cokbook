#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 06/11/2018.


p = (4, 5)
x, y = p
print(x, y)

data = ["ACME", 50, 91.1, (2012, 12, 21)]

name, shares, price, date = data

print(name)

print(date)

name, shares, price, (year, mon, day) = data

print(name)
print(year)
print(mon)
print(day)

p = (4, 5)
# x,y,z = p   error


s = "hello"

a,b,c,d,e = s

print(a,b,c,d,e)

data = ["ACME", 50, 91.1, (2012, 12, 21)]

_, shares, price, _ = data





