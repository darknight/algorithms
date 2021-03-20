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
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        refer to https://leetcode.com/problems/daily-temperatures/discuss/136017/Elegant-Python-Solution-with-Stack
        """
        if len(T) <= 1:
            return [0]
        res = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while len(stack) > 0 and t > T[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
            print(i, t, res)

        return res


if __name__ == '__main__':
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
