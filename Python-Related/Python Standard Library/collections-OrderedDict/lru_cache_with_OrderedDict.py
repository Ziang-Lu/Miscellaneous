#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
OrderedDict with access-order to model an LRU cache.
"""

__author__ = 'Ziang Lu'

from collections import OrderedDict


class LRUCache(OrderedDict):
    """
    Limit size, evicting the least recently looked-up key when full.
    """
    __slots__ = ['_cache_size']

    def __init__(self, cache_size: int=128, *args, **kwargs):
        """
        Constructor with parameter.
        :param cache_size: int
        """
        self._cache_size = cache_size
        super().__init__(*args, **kwargs)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        # Note that since we need to keep access-order, we need to move the
        # accessed node to the end
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        # Note that since we need to keep access-order, we need to move the
        # accessed node to the end
        self.move_to_end(key)
        if len(self) > self._cache_size:  # When full
            # Evect the least recently looked-up key
            eldest = next(iter(self))
            del self[eldest]
