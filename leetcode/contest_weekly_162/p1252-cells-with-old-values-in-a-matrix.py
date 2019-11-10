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
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        n, m = m, n

        matrix = []
        for _ in range(m):
            matrix.append([0] * n)

        for idx in indices:
            row, col = idx[0], idx[1]
            for j in range(n):
                matrix[row][j] += 1
            for i in range(m):
                matrix[i][col] += 1

        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] % 2 == 1:
                    res += 1

        return res


if __name__ == '__main__':
    assert Solution().oddCells(2, 3, [[0,1],[1,1]]) == 6
