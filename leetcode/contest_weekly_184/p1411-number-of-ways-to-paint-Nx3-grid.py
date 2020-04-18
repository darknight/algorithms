#!/usr/bin/env python3

import math, itertools, functools, heapq, re
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass


class Solution:
    def WA_numOfWays(self, n: int) -> int:
        """
        maximum recursion depth exceeded
        """
        state = {
            1: [2,3,5,6,11,12],
            2: [1,4,7,9,10,12],
            3: [1,4,7,8],
            4: [2,3,8,11],
            5: [1,7,9,10],
            6: [1,4,7,8,10,11],
            7: [2,3,5,6,11,12],
            8: [3,4,6,12],
            9: [2,5,10,11],
            10: [5,6,9,12],
            11: [1,4,6,9,12],
            12: [2,7,8,10,11]
        }

        @functools.lru_cache(None)
        def dfs(row: int, s: int) -> int:
            if row == 1:
                return 1
            res = 0
            for v in state[s]:
                res += dfs(row-1, v)
            return res

        total = 0
        for i in range(1, 13):
            total += dfs(n, i)

        return total % (10 ** 9 + 7)


    def numOfWays(self, n: int) -> int:
        """
        refer to
        https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/discuss/574923/JavaC%2B%2BPython-DP-O(1)-Space
        """
        a121 = 6
        a123 = 6
        for _ in range(1, n):
            b121 = a121 * 3 + a123 * 2
            b123 = a121 * 2 + a123 * 2
            a121, a123 = b121, b123

        return (a121+a123) % (10**9 + 7)




if __name__ == '__main__':
    print(Solution().numOfWays(1))
    print(Solution().numOfWays(2))
    print(Solution().numOfWays(3))
    print(Solution().numOfWays(7))
    print(Solution().numOfWays(5000))
