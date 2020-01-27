#!/usr/bin/env python3

import math, itertools
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
        M = len(mat)
        N = len(mat[0])
        for row in range(M - 1, -1, -1):
            col = 0
            self.reorder(row, col, M, N, mat)
        for col in range(1, N):
            row = 0
            self.reorder(row, col, M, N, mat)

        return mat

    def reorder(self, row, col, M, N, mat):
        line = []
        i = row
        j = col
        while i < M and j < N:
            line.append(mat[i][j])
            i += 1
            j += 1
        line.sort()
        i = row
        j = col
        while i < M and j < N:
            mat[i][j] = line.pop(0)
            i += 1
            j += 1

if __name__ == '__main__':
    print(Solution().diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
    print(Solution().diagonalSort([[1,2,3],[4,5,6],[7,8,9],[0,1,2]]))
