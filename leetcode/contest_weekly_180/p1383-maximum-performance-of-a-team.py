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
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        calls = [0]

        @functools.lru_cache(None)
        def dfs(curr: int, total: int, accu_s: int, min_e: int) -> int:
            # calls[0] += 1
            # print(calls)
            print(curr, total, accu_s, min_e)
            if total > k:
                return 0
            if curr >= n:
                return 0
            # take curr
            res = (accu_s+speed[curr]) * min(min_e, efficiency[curr])
            res = max(res, dfs(curr+1, total+1, accu_s+speed[curr], min(min_e, efficiency[curr])))
            # not take curr
            for i in range(curr+1, n):
                res = max(res, dfs(i, total, accu_s, min_e))

            return res

        result = dfs(0, 0, 0, math.inf)
        print(result)
        return result


if __name__ == '__main__':
    assert Solution().maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2) == 60
    # assert Solution().maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3) == 68
    # assert Solution().maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4) == 72

    # at most k
    # assert Solution().maxPerformance(3,[2,8,2],[2,7,1],2) == 56