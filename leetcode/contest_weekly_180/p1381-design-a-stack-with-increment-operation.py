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


class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.size = 0
        self.stack = []

    def push(self, x: int) -> None:
        if self.size < self.max_size:
            self.size += 1
            self.stack.append(x)

    def pop(self) -> int:
        if self.size == 0:
            return -1
        self.size -= 1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        limit = min(k, self.size)
        for i in range(limit):
            self.stack[i] += val


if __name__ == '__main__':
    pass
