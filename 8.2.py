#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 07/12/2018.
_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        if format_spec == "":
            format_spec = "ymd"

        fmt = _formats[format_spec]
        return fmt.format(d=self)


d = Date(2012, 12, 21)

print(format(d))