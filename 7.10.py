#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 07/12/2018.


def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


def print_result(result):
    print("Got: ", result)


def add(x, y):
    return x + y


apply_async(add, (2, 3), callback=print_result)


class ResultHandler:
    def __init__(self):
        self.squence = 0

    def handler(self, result):
        self.squence += 1
        print("[{}] Got: {}".format(self.squence, result))


r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)
apply_async(add, (2, 3), callback=r.handler)
apply_async(add, (2, 3), callback=r.handler)
apply_async(add, (2, 3), callback=r.handler)
