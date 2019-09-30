#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List


class Solution:

    def TLE_equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        if maxCost <= 0 or len(s) == 0:
            return 1

        diff = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        cost_forth = [0] * len(diff)
        cost_back = [0] * len(diff)

        cost_forth[0] = diff[0]
        for i in range(1, len(diff)):
            cost_forth[i] = cost_forth[i-1] + diff[i]

        cost_back[-1] = diff[-1]
        for i in range(-2, -len(diff)-1, -1):
            cost_back[i] = cost_back[i+1] + diff[i]

        total = sum(diff)
        res = 0

        for i in range(len(diff)):
            for j in range(i, len(diff)):
                cost = cost_forth[j] + cost_back[i] - total
                if cost <= maxCost:
                    res = max(res, j-i+1)

        return res

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        sliding window
        took long time to solve it
        """
        if maxCost <= 0 or len(s) == 0:
            return 1

        diff = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        start = 0
        end = 0
        cost = 0
        res = 0
        print(diff)
        while end < len(diff):
            if cost + diff[end] <= maxCost:
                cost += diff[end]
                end += 1
                res = max(res, end - start)
            else:
                cost += diff[end]
                end += 1
                while cost > maxCost:
                    cost -= diff[start]
                    start += 1

        return res


if __name__ == '__main__':
    assert Solution().equalSubstring("abcd", "bcdf", 3) == 3
    assert Solution().equalSubstring("abcd", "cdef", 3) == 1
    assert Solution().equalSubstring("abcd", "abce", 0) == 1
    assert Solution().equalSubstring("abcd", "acde", 0) == 1
    assert Solution().equalSubstring("abcd", "cdef", 1) == 0
    assert Solution().equalSubstring("krrgw", "zjxss", 19) == 2
    assert Solution().equalSubstring("krpgjbjjznpzdfy","nxargkbydxmsgby", 14) == 4
