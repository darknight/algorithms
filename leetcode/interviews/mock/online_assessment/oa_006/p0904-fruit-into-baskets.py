#!/usr/bin/env python3

import math
import itertools
from collections import defaultdict
from collections import Counter
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass

try:
    from _list import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass


class Solution:
    def WA_totalFruit(self, tree: List[int]) -> int:
        size = len(tree)
        if size == 1:
            return 1
        t1 = tree[0]
        last1 = 0
        cnt1 = 1
        t2 = -1
        last2 = -1
        cnt2 = 0
        res = 0
        for i in range(1, size):
            if tree[i] == t1:
                last1 = i
                cnt1 += 1
            elif tree[i] == t2:
                last2 = i
                cnt2 += 1
            else: # reset one of baskets
                if t2 == -1 or last2 < last1:
                    t2 = tree[i]
                    last2 = i
                    cnt2 = 1
                else:
                    t1 = tree[i]
                    last1 = i
                    cnt1 = 1
            res = max(res, cnt1 + cnt2)

        return res

    def totalFruit(self, tree: List[int]) -> int:
        """
        refer to
        https://leetcode.com/problems/fruit-into-baskets/discuss/170737/Python-sliding-window
        """
        size = len(tree)
        if size == 1:
            return 1
        res = 0
        c = Counter()
        l = 0
        for r in range(size):
            c[tree[r]] += 1
            while len(c) > 2:
                c[tree[l]] -= 1
                if c[tree[l]] == 0:
                    del c[tree[l]]
                l += 1

            res = max(res, r - l + 1)

        return res



if __name__ == '__main__':
    assert Solution().totalFruit([1,2,1]) == 3
    assert Solution().totalFruit([0,1,2,2]) == 3
    assert Solution().totalFruit([1,2,3,2,2]) == 4
    assert Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]) == 5
    assert Solution().totalFruit([1,2]) == 2
    assert Solution().totalFruit([1,1]) == 2
    assert Solution().totalFruit([1,0,1,4,1,4,1,2,3]) == 5
