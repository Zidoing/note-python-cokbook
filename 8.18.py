#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 10/12/2018.


class LoggedMappingMixin:
    __slots__ = ()

    def __getitem__(self, item):
        print("getting " + str(item))
        return super(LoggedMappingMixin, self).__getitem__(item)

    def __setitem__(self, key, value):
        print("setting {} = {!r} ".format(key, value))
        return super(LoggedMappingMixin, self).__setitem__(key, value)

    def __delitem__(self, key):
        print("deleting " + str(key))
        return super(LoggedMappingMixin, self).__delitem__(key)


class SetOnceMappingMixin:
    '''
    Only allow a key to be set once.
    '''
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)


class StringKeysMappingMixin:
    '''
    Restrict keys to strings only
    '''
    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('keys must be strings')
        return super().__setitem__(key, value)


class LoggedDict(LoggedMappingMixin, dict):
    pass


d = LoggedDict()

d["x"] = 23
print(d["x"])

del d["x"]


def LoggedMapping(cls):
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self, key):
        print("Getting" + str(key))
        return cls_getitem(self, key)

    cls.__getitem__ = __getitem__

    return cls


@LoggedMapping
class LoggedDict(dict):
    pass
