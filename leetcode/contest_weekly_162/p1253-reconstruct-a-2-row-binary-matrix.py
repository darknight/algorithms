#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set

try:
    from _tree import *
except ImportError:
    pass


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        total = sum(colsum)
        if total != upper + lower:
            return []

        size = len(colsum)
        num1 = 0
        num2 = 0
        for n in colsum:
            if n == 1:
                num1 += 1
            if n == 2:
                num2 += 1

        low1 = 0
        low2 = 0
        up1 = 0
        up2 = 0
        if num2 >= upper // 2:
            up2 = upper // 2
            up1 = upper % 2
            low2 = num2 - up2
            low1 = num1 - up1
        else:
            up2 = num2
            up1 = upper - up2 * 2
            low2 = 0
            low1 = num1 - up1

        print(up1, up2, low1, low2)
        res = [[0] * size, [0] * size]
        for j in range(size):
            if colsum[j] == 0:
                continue
            if colsum[j] == 2:
                if up2 > 0:
                    res[0][j] = 2
                    up2 -= 1
                else:
                    res[1][j] = 2
                    low2 -= 1
            else:
                if up1 > 0:
                    res[0][j] = 1
                    up1 -= 1
                else:
                    res[1][j] = 1
                    low1 -= 1

        assert up1 == up2 == low1 == low2 == 0

        print(res)
        return res


if __name__ == '__main__':
    # Solution().reconstructMatrix(2, 1, [1, 1, 1])
    # Solution().reconstructMatrix(2, 3, [2, 2, 1, 1])
    # Solution().reconstructMatrix(5, 5, [2, 1, 2, 0, 1, 0, 1, 2, 0, 1])

    Solution().reconstructMatrix(5, 1, [0,1,0,1,2,1,1])