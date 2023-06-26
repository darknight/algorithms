#!/usr/bin/env python3

import math, itertools, functools, heapq
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple

try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass


class LRUCache(object):
    # TODO: slow, improve
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.queue = []

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache:
            self.queue.remove(key)
            self.queue.insert(0, key)
            return self.cache[key]
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key not in self.cache:
            if len(self.queue) < self.capacity:
                self.queue.insert(0, key)
            else:
                k = self.queue.pop()
                del self.cache[k]
                self.queue.insert(0, key)
        else:
            self.queue.remove(key)
            self.queue.insert(0, key)
        self.cache[key] = value


class LRUCacheV2:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.map: Dict[int, DoubleListNode] = {}

    def _move_to_head(self, node: DoubleListNode):
        if self.head is node:  # head node
            return
        elif self.tail is node:  # tail node
            self.tail = node.prev
            if node.prev is not None:
                node.prev.next = None
        else:  # middle node
            node.prev.next = node.next
            node.next.prev = node.prev
        node.prev = None
        node.next = None
        self._insert_head(node)

    def _insert_head(self, node: DoubleListNode):
        if self.head is None or self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._move_to_head(node)
        else:
            node = DoubleListNode(key=key, val=value)
            self.map[key] = node
            self._insert_head(node)
            if len(self.map) > self.capacity:  # evict
                del self.map[self.tail.key]
                self.tail = self.tail.prev
        print(self.map)


class LRUCacheOfficial:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DoubleListNode(-1, -1)
        self.tail = DoubleListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map: Dict[int, DoubleListNode] = {}

    def _remove(self, node: DoubleListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node: DoubleListNode):
        next_head = self.head.next
        next_head.prev = node
        node.next = next_head
        node.prev = self.head
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            old_node = self.map[key]
            self._remove(old_node)

        node = DoubleListNode(key=key, val=value)
        self.map[key] = node
        self._add(node)

        if len(self.map) > self.capacity:
            node_to_delete = self.tail.prev
            self._remove(node_to_delete)
            del self.map[node_to_delete.key]


if __name__ == '__main__':
    lru = LRUCacheOfficial(capacity=2)
    lru.put(1, 1)
    lru.put(2, 2)
    print("%d==1" % lru.get(1))
    lru.put(3, 3)
    print("%d==-1" % lru.get(2))
    lru.put(4, 4)
    print("%d==-1" % lru.get(1))
    print("%d==3" % lru.get(3))
    print("%d==4" % lru.get(4))

    lru = LRUCacheOfficial(capacity=3)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.put(3, 3)
    lru.put(4, 4)
    print("%d==4" % lru.get(4))
    print("%d==3" % lru.get(3))
    print("%d==2" % lru.get(2))
    print("%d==-1" % lru.get(1))
    lru.put(5, 5)
    print("%d==-1" % lru.get(1))
    print("%d==2" % lru.get(2))
    print("%d==3" % lru.get(3))
    print("%d==-1" % lru.get(4))
    print("%d==5" % lru.get(5))
