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
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        if rows == 1 or cols == 1:
            return mat

        for row_start in range(rows-1, 0, -1):
            tmp = []
            i = row_start
            j = 0
            while i < rows and j < cols:
                tmp.append(mat[i][j])
                i += 1
                j += 1
            tmp.sort()
            i = row_start
            j = 0
            while i < rows and j < cols:
                mat[i][j] = tmp.pop(0)
                i += 1
                j += 1

        for col_start in range(cols):
            tmp = []
            i = 0
            j = col_start
            while i < rows and j < cols:
                tmp.append(mat[i][j])
                i += 1
                j += 1
            tmp.sort()
            i = 0
            j = col_start
            while i < rows and j < cols:
                mat[i][j] = tmp.pop(0)
                i += 1
                j += 1

        return mat


    def diagonalSort_official(self, mat: List[List[int]]) -> List[List[int]]:
        """
        row-col in one diagonal is the same, so can act as key of Map[int, list]
        """
        rows = len(mat)
        cols = len(mat[0])

        diagonals = defaultdict(list)

        for row in range(rows):
            for col in range(cols):
                diagonals[row-col].append(mat[row][col])

        for diag in diagonals.values():
            heapq.heapify(diag)

        for row in range(rows):
            for col in range(cols):
                value = heapq.heappop(diagonals[row-col])
                mat[row][col] = value

        return mat


if __name__ == '__main__':
    s = Solution()
    res = s.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]])
    print(res)
