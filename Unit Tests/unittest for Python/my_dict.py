#!usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Ziang Lu'

from typing import Any


class MyDict(dict):
    """
    An dictionary class that acts the same as "dict", but also allows accessing
    values by keys as attributes.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, key: Any) -> Any:
        try:
            return self[key]
        except KeyError:
            # To let this dict act like a class, transform KeyError to
            # ArributeError
            raise AttributeError("'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key: Any, val: Any) -> None:
        self[key] = val
