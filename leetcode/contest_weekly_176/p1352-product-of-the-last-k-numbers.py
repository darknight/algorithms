#!/usr/bin/env python3

import math, itertools, functools
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass


class TLE_ProductOfNumbers:

    def __init__(self):
        self.lists = []
        self.refresh = False
        self.cache = defaultdict(int)
        self.curr_k = 0

    def add(self, num: int) -> None:
        self.lists.append(num)
        self.refresh = True

    def getProduct(self, k: int) -> int:
        if self.refresh is True:
            self.refresh = False
            self.cache.clear()
            res = 1
            for i in range(1, k + 1):
                res = res * self.lists[-i]
                self.cache[i] = res
            self.curr_k = k

            return res
        else:
            if k <= self.curr_k:
                return self.cache[k]
            else:
                res = self.cache[self.curr_k]
                for i in range(self.curr_k+1, k + 1):
                    res = res * self.lists[-i]
                    self.cache[i] = res

        return res


class TLE_2_ProductOfNumbers:

    def __init__(self):
        self.lists = []

    def add(self, num: int) -> None:
        for i in range(len(self.lists)):
            self.lists[i] = self.lists[i] * num
        self.lists.append(num)

    def getProduct(self, k: int) -> int:
        return self.lists[-k]


class ProductOfNumbers:
    """
    refer to
    https://leetcode.com/problems/product-of-the-last-k-numbers/discuss/510260/JavaC%2B%2BPython-Prefix-Product
    """
    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            last = self.prefix[-1] * num
            self.prefix.append(last)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        res = self.prefix[-1] / self.prefix[-k-1]
        return res


if __name__ == '__main__':
    p = ProductOfNumbers()
    p.add(7)
    assert p.getProduct(1) == 7
    p.add(5)
    p.add(0)
    p.add(4)
    assert p.getProduct(4) == 0
    assert p.getProduct(3) == 0
    assert p.getProduct(1) == 4

    q = ProductOfNumbers()
    q.add(4)
    q.add(9)
    assert q.getProduct(2) == 36
    assert q.getProduct(1) == 9
    q.add(3)
    q.add(1)
    assert q.getProduct(1) == 1
    assert q.getProduct(1) == 1
    assert q.getProduct(2) == 3
    assert q.getProduct(3) == 27
    q.add(2)
    assert q.getProduct(5) == 216
