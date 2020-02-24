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


class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.cnt = 0
        self.discount = discount

        mapping = {}
        for i in range(len(products)):
            id = products[i]
            price = prices[i]
            mapping[id] = price
        self.mapping = mapping

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.cnt += 1
        discount = 0
        if self.cnt == self.n:
            self.cnt = 0
            discount = self.discount

        total = 0
        for i in range(len(product)):
            price = self.mapping[product[i]]
            total += price * amount[i]

        return total - total * discount / 100





if __name__ == '__main__':
    pass
