#!/usr/bin/env python3

import math, itertools, functools, heapq
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple


class Solution:

    def calc_repeat(self, mat: List[List[int]]) -> int:
        res = 0
        for row in mat:
            if len(row) != len(set(row)):
                res += 1

        return res

    def calc_trace(self, mat: List[List[int]], N: int) -> Tuple[int, int, int]:
        row = self.calc_repeat(mat)
        trace = 0
        for i in range(N):
            for j in range(i, N):
                if i == j:
                    trace += mat[i][j]
                else:
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        col = self.calc_repeat(mat)

        return trace, row, col



if __name__ == '__main__':
    s = Solution()
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        mat = [list(map(int, input().split())) for _ in range(N)]
        k, r, c = s.calc_trace(mat, N)
        print("Case #{}: {} {} {}".format(i, k, r, c))
