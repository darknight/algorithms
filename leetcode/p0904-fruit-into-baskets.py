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
    def AC_totalFruit(self, tree: List[int]) -> int:
        N = len(tree)
        if N <= 2:
            return N
        res = 0
        a, a_cnt, a_end = tree[0], 1, 0
        b, b_cnt, b_end = -1, 0, -1
        for i in range(1, N):
            if tree[i] == a:
                a_cnt += 1
                a_end = i
                continue
            if b == -1:
                b = tree[i]
                b_cnt = 1
                b_end = i
                continue
            else:
                if tree[i] == b:
                    b_cnt += 1
                    b_end = i
                else:  # replace a or b
                    res = max(res, a_cnt+b_cnt)
                    if tree[i-1] == a:
                        a_cnt = a_end - b_end
                        b = tree[i]
                        b_cnt = 1
                        b_end = i
                    else:
                        b_cnt = b_end - a_end
                        a = tree[i]
                        a_cnt = 1
                        a_end = i
        return max(res, a_cnt+b_cnt)

    def totalFruit(self, tree: List[int]) -> int:
        """
        sliding window
        refer to: https://leetcode.com/problems/fruit-into-baskets/discuss/170764/Java-Sliding-Window-Illustration
        """
        N = len(tree)
        if N <= 2:
            return N
        count = Counter()
        res, i = 0, 0
        for j, v in enumerate(tree):
            count[v] += 1
            while len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            res = max(res, j - i + 1)

        return res


if __name__ == '__main__':
    print(Solution().totalFruit([1,2,1]))
    print(Solution().totalFruit([0,1,2,2]))
    print(Solution().totalFruit([1,2,3,2,2]))
    print(Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
    print(Solution().totalFruit([0,0,1,1]))

