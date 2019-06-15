#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
OrderedDict demo.
It is very similar to LinkedHashMap in Java.
"""

__author__ = 'Ziang Lu'

from collections import OrderedDict
from typing import Any


def put_entries_to_map(map_: dict) -> None:
    """
    Puts some entries to the given map.
    :param map_: dict
    """
    map_[1] = 'a'
    map_[4] = 'd'
    map_[2] = 'b'
    print(map_)
    map_[4] = 'new d'
    print(map_)


class AccessOrderedDict(OrderedDict):
    """
    An OrderedDict with access-order, not insertion-order.
    """
    __slots__ = []

    def __setitem__(self, key: Any, value: Any):
        super().__setitem__(key, value)
        # Note that since we need to keep access-order, we need to move the
        # accessed node to the end
        super().move_to_end(key)


def main():
    print('===== dict demo =====')
    d = {}
    put_entries_to_map(d)

    print()

    print('===== OrderedDict demo =====')
    ordered_d = OrderedDict()
    put_entries_to_map(ordered_d)

    print()

    print('===== OrderedDict (with access-order) demo =====')
    ordered_d_access_order = AccessOrderedDict()
    put_entries_to_map(ordered_d_access_order)


if __name__ == '__main__':
    main()


# Output:
# ===== dict demo =====
# {1: 'a', 2: 'b', 4: 'd'}
# {1: 'a', 2: 'b', 4: 'new d'}

# ===== OrderedDict demo =====
# OrderedDict([(1, 'a'), (4, 'd'), (2, 'b')])
# OrderedDict([(1, 'a'), (4, 'new d'), (2, 'b')])

# ===== OrderedDict (with access-order) demo =====
# AccessOrderedDict([(1, 'a'), (4, 'd'), (2, 'b')])
# AccessOrderedDict([(1, 'a'), (2, 'b'), (4, 'new d')])
