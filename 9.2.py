#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 11/12/2018.

import time

from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(func.__name__, end - start)

        return result

    return wrapper


@timethis
def countdown(n: int):
    """
    countdown
    :param n:
    :return:
    """
    while n > 0:
        n -= 1


countdown(1000)
print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)

print(countdown.__wrapped__(1000))


@timethis
def add(x, y):
    return x + y


print(add(3, 4))

orig_add = add.__wrapped__

print(orig_add)
print(orig_add(3, 4))


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("b decorator 1")
        result = func(*args, **kwargs)
        print("e decorator 1")
        return result

    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("b decorator 2")
        result = func(*args, **kwargs)
        print("e decorator 2")
        return result

    return wrapper


@decorator1
@decorator2
def add(x, y):
    return x + y


add(3, 4)
