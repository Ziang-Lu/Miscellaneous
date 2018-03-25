#!usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Ziang Lu'


class MyDict(dict):
    """
    An dictionary class that acts the same as "dict", but also allows accessing
    values by keys as attributes.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            # To let this dict act like a class, transform KeyError to
            # ArributeError
            raise AttributeError("'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, val):
        self[key] = val
