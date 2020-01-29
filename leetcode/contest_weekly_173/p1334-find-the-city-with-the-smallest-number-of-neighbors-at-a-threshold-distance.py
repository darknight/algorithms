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
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        mat = []
        for _ in range(n):
            mat.append([math.inf] * n)
        for i in range(n):
            mat[i][i] = 0
        for edge in edges:
            u, v, weight = edge
            mat[u][v] = weight
            mat[v][u] = weight

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if mat[i][k] + mat[k][j] < mat[i][j]:
                        mat[i][j] = mat[i][k] + mat[k][j]
        num = math.inf
        res = -1
        for u in range(n):
            cites = [v for v in range(n) if mat[u][v] <= distanceThreshold]
            if len(cites) <= num:
                num = len(cites)
                res = u

        return res


if __name__ == '__main__':
    assert Solution().findTheCity(n = 4,
                                  edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]],
                                  distanceThreshold = 4) == 3
    assert Solution().findTheCity(n = 5,
                                  edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]],
                                  distanceThreshold = 2) == 0
