#!/usr/bin/env python3

import math, itertools
from collections import defaultdict, Counter
from typing import List, Set

try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass


class Solution:
    def TIMEOUT_gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        table = []
        for i in range(N + 1):
            table.append([])

        for path in paths:
            v, w = path[0], path[1]
            table[v].append(w)
            table[w].append(v)

        res = [0] * (N + 1)

        for v in range(1, N + 1):
            if res[v] == 0:
                res[v] = 1
                self.dfs(v, table, res)

    def dfs(self, v: int, table: List[List[int]], res: List[int]):
        for w in table[v]:
            if res[w] == 0:
                res[w] = (res[v]) % 4 + 1
                self.dfs(w, table, res)

    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        """
        refer to
        https://leetcode.com/problems/flower-planting-with-no-adjacent/discuss/290930/Python-Greedy-Concise-%2B-Explanation
        """
        table = []
        for i in range(N + 1):
            table.append([])

        for path in paths:
            v, w = path[0], path[1]
            table[v].append(w)
            table[w].append(v)

        res = [0] * (N + 1)

        for v in range(1, N + 1):
            if res[v] > 0:
                continue
            used = set()
            for w in table[v]:
                if res[w] > 0:
                    used.add(res[w])
            for t in range(1, 5):
                if t not in used:
                    res[v] = t
                    break

        return res[1:]



if __name__ == '__main__':
    Solution().gardenNoAdj(N = 3, paths = [[1,2],[2,3],[3,1]])
    Solution().gardenNoAdj(N = 4, paths = [[1,2],[3,4]])
    Solution().gardenNoAdj(N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]])
