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


class Solution:
    def asteroidCollision_messy(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        i = 1
        while i < len(asteroids):
            nxt = asteroids[i]
            if len(stack) == 0 or stack[-1] * nxt > 0:
                stack.append(nxt)
                i += 1
                continue
            if stack[-1] + nxt == 0:
                if stack[-1] > 0:  # explode must be positive then negative
                    stack.pop()
                else:
                    stack.append(nxt)
                i += 1
                continue
            if stack[-1] < 0:
                stack.append(nxt)
                i += 1
                continue
            while len(stack) > 0 and stack[-1] > 0:
                if stack[-1] == abs(nxt):
                    stack.pop()
                    i += 1
                    break
                if stack[-1] < abs(nxt):
                    stack.pop()
                else:
                    i += 1
                    break
        return stack

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            nxt = asteroids[i]
            if len(stack) == 0:
                stack.append(nxt)
                i += 1
                continue
            while len(stack) > 0:
                if stack[-1] < 0 or nxt > 0:
                    stack.append(nxt)
                    i += 1
                    break
                if stack[-1] == abs(nxt):
                    i += 1
                    stack.pop()
                    break
                if stack[-1] < abs(nxt):
                    stack.pop()
                else:
                    i += 1
                    break
        return stack


if __name__ == '__main__':
    pass
