#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 07/11/2018.


from collections import defaultdict

d = defaultdict(list)

d["a"].append(1)
d["a"].append(2)
d["a"].append(4)
d["b"].append(5)
print(d)

d = {}

d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('a', []).append(43)

print(d)
