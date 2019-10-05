#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List


class Solution:
    def TLE_nthUglyNumber(self, n: int) -> int:
        """refer to other solution"""
        res = [1] * n
        found = {1}
        for i in range(1, n):
            next_num = math.inf
            for j in range(len(res)):
                m2 = res[j] * 2
                m3 = res[j] * 3
                m5 = res[j] * 5
                if m2 not in found:
                    next_num = min(next_num, m2)
                if m3 not in found:
                    next_num = min(next_num, m3)
                if m5 not in found:
                    next_num = min(next_num, m5)
            res[i] = next_num
            found.add(next_num)
        # print(res)
        return res[-1]

    def nthUglyNumber(self, n: int) -> int:
        """refer to other solution"""
        res = [1] * n
        i2 = 0
        i3 = 0
        i5 = 0
        for i in range(1, n):
            next_num = min(res[i2] * 2, res[i3] * 3, res[i5] * 5)
            res[i] = next_num
            while res[i2] * 2 <= next_num:
                i2 += 1
            while res[i3] * 3 <= next_num:
                i3 += 1
            while res[i5] * 5 <= next_num:
                i5 += 1
        # print(res)
        return res[-1]

if __name__ == '__main__':
    assert Solution().nthUglyNumber(1) == 1
    assert Solution().nthUglyNumber(2) == 2
    assert Solution().nthUglyNumber(3) == 3
    assert Solution().nthUglyNumber(4) == 4
    assert Solution().nthUglyNumber(5) == 5
    assert Solution().nthUglyNumber(10) == 12
    assert Solution().nthUglyNumber(11) == 15
    assert Solution().nthUglyNumber(320) == 110592
    assert Solution().nthUglyNumber(1690) == 2123366400
