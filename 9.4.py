#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 11/12/2018.


from functools import wraps

import logging


def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)

        logmsg = message if message else func.__name__
        print(logname, logmsg)
        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


add(2, 3)


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


spam()
