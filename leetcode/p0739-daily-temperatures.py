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
    def dailyTemperatures_TLE(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if n == 1:
            return [0]
        result = [0] * n
        for i in range(n-1):
            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break

        return result

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        hint: Monotonic Stack
        """
        n = len(temperatures)
        if n == 1:
            return [0]
        result = [0] * n
        stack = [0]
        for j in range(1, n):
            print(stack, temperatures[j])
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[j]:
                i = stack.pop()
                result[i] = j - i
            stack.append(j)

        return result

if __name__ == '__main__':
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
