#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-18.


import ast

ex = ast.parse("2 + 3*4 + x", mode="eval")


print(ex)


print(ast.dump(ex))


