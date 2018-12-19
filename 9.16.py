#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-18.


from inspect import Signature, Parameter

params = [

    Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
    Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
    Parameter('z', Parameter.KEYWORD_ONLY, default=None),

]

sig = Signature(params)

print(sig)


def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)

    items = bound_values.arguments.items()
    print(bound_values.arguments)
    for name, value in items:
        print(name, value)


func(1, 2, z=3)
