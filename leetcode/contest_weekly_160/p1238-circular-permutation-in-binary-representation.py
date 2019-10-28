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
    def circularPermutation(self, n: int, start: int) -> List[int]:
        s = []
        if n == 1:
            s = [0, 1]
        elif n == 2:
            s = [0, 1, 3, 2]
        else:
            s = [0, 1, 3, 2]
            for k in range(3, n + 1):
                size = len(s)
                significant = 2 ** (k - 1)
                for i in range(size - 1, -1, -1):
                    s.append(significant + s[i])

        # print(s)
        idx = s.index(start)
        res = s[idx:] + s[0:idx]
        # print(res)

        return res


if __name__ == '__main__':
    assert Solution().circularPermutation(1, 1) == [1, 0]
    # assert Solution().circularPermutation(2, 3) == [3, 2, 0, 1]
    # assert Solution().circularPermutation(3, 2) == [2, 6, 7, 5, 4, 0, 1, 3]
