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
    def minimumSwap(self, s1: str, s2: str) -> int:
        if len(s1) != len(s2):
            return -1

        size = len(s1)

        xcnt = 0
        ycnt = 0
        for c in s1:
            if c == 'x':
                xcnt += 1
            else:
                ycnt += 1

        for c in s2:
            if c == 'x':
                xcnt += 1
            else:
                ycnt += 1

        if xcnt % 2 != 0 or ycnt % 2 != 0:
            return -1

        xy = 0
        yx = 0
        for i in range(size):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    xy += 1
                else:
                    yx += 1

        return xy // 2 + yx // 2 + (xy % 2) * 2




if __name__ == '__main__':
    assert Solution().minimumSwap("xx", "yy") == 1
    assert Solution().minimumSwap("xy", "yx") == 2
    assert Solution().minimumSwap("xx", "xy") == -1
    assert Solution().minimumSwap("xxyyxyxyxx", "xyyxyxxxyx") == 4
