#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 11/12/2018.


from functools import wraps, partial

import logging


def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        print('fdsa')
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper


@logged()
def add(x, y):
    return x + y



print(add(3,3))