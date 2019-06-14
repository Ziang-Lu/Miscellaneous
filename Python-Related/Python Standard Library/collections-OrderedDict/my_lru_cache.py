#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
My LRU cache demo.
"""

__author__ = 'Ziang Lu'

from typing import Any


class ItemNode:
    """
    ItemNode class.
    """
    __slots__ = ['_key', '_val']

    def __init__(self, key: Any, val: Any):
        """
        Constructor with parameter.
        :param key: Any
        :param val: Any
        """
        self._key = key
        self._val = val
        self._prev = None
        self._next = None

    @property
    def key(self) -> Any:
        """
        Accessor of key.
        :return: Any
        """
        return self._key

    @property
    def value(self) -> Any:
        """
        Accessor of val.
        :return: Any
        """
        return self._val

    @property
    def prev(self) -> ItemNode:
        return self._prev

    @property
    def next(self) -> ItemNode:
        return self._next


class MyLRUCache(dict):
    """
    My LRU Cache.
    The idea is to decorate a dict with a doubly linked-list to keep track of
    the access-order of the items.
    """
    __slots__ = ['_head', '_end', '_cache_size']

    def __init__(self, cache_size: int):
        """
        Constructor with parameter.
        :param cache_size: int
        """
        self._head = None
        self._end = None
        self._cache_size = cache_size

    def __getitem__(self, key):
        if key not in self:
            return None
        node = super().__getitem__(key)
        self._move_node_to_end(node)
        return node.value

    def _move_node_to_end(self, node: ItemNode) -> None:
        """
        Private helper method to move the given node to the end of the doubly
        linked-list.
        :param node: ItemNode
        """
        if node is self._end:  # No need to move
            return
        if node is self._head:  # Simply remove and reset the head
            head_next = self._head.next
            self._head.next = None
            head_next.prev = None
            self._head = head_next
        else:  # Remove the given node by reconnecting the previous and next nodes
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None
        self._add_node_to_end(node)

    def _add_node_to_end(self, node: ItemNode) -> None:
        """
        Helper method to add the given node to the end of the doubly
        linked-list.
        :param node: ItemNode
        """
        if not self._head and not self._end:
            self._head = node
        # Add the given node and reset the end
        self._end.next = node
        node.prev = self._end
        self._end = node

    def __setitem__(self, key, value):
        if key in self:
            node = super().__getitem__(key)
            node.val = value
            self._move_node_to_end(node)
        else:
            if len(self) >= self._cache_size:  # Reach cache limit
                # Remove the least recently used item
                super().remove(self._head.key)
                head_next = self._head.next
                if head_next:
                    head_next.prev = None
                self._head = head_next
            # Add the new node
            new_node = ItemNode(key, value)
            super().__setitem__(key, new_node)
            self._add_node_to_end(new_node)
