#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 11/12/2018.


from functools import wraps, partial

import logging


def attach_wrapper(obj, func=None):
    if func is None:
        print('s')
        print(attach_wrapper)
        result = partial(attach_wrapper, obj)
        print(result)
        return result

    setattr(obj, func.__name__, func)

    return func


def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper

    return decorate


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


# spam.set_message = "fadsfd"
# a = spam()
#
