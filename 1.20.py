# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 26/11/2018.


a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = {'xy': 2, 'z': 4}


from collections import ChainMap



d = ChainMap(a,b,c)




print(d)


for i in d:
    print(i), print(d[i])


print(len(d))
