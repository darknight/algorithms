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
    def TLE_numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1:
            return 0
        mat = []
        for _ in range(n):
            mat.append([0] * n)

        for i in range(n):
            parent = manager[i]
            if parent == -1:
                continue
            mat[parent][i] = 1

        for i in range(n):
            time = informTime[i]
            if time == 0:
                continue
            for j in range(n):
                if mat[i][j] == 1:
                    mat[i][j] = time

        def dfs(node: int, t: int) -> int:
            tmp = 0
            for child in range(n):
                if mat[node][child] > 0:
                    tmp = max(tmp, dfs(child, t+mat[node][child]))
            return max(t, tmp)

        res = dfs(headID, 0)
        return res


    def TLE_2_numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1:
            return 0
        mat = []
        for _ in range(n):
            mat.append({})

        for i in range(n):
            parent = manager[i]
            if parent == -1:
                continue
            mat[parent][i] = 0

        for i in range(n):
            time = informTime[i]
            if time == 0:
                continue
            for j in range(n):
                if j in mat[i]:
                    mat[i][j] = time

        def dfs(node: int, t: int) -> int:
            tmp = 0
            for (child, weight) in mat[node].items():
                tmp = max(tmp, dfs(child, t+weight))
            return max(t, tmp)

        res = dfs(headID, 0)
        return res


    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """refer to
        https://leetcode.com/problems/time-needed-to-inform-all-employees/discuss/532530/Python3-Easy-Python-Solution%3A-DijkstraBFSDFS
        """
        if n == 1:
            return 0
        mat = [[] for _ in range(n)]

        for i in range(n):
            if manager[i] == -1:
                continue
            mat[manager[i]].append(i)

        res = [0]

        def dfs(node: int, t: int):
            print(node, t)
            res[0] = max(res[0], t)
            for child in mat[node]:
                dfs(child, t + informTime[node])

        dfs(headID, 0)
        return res[0]


if __name__ == '__main__':
    assert Solution().numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]) == 1
    assert Solution().numOfMinutes(n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]) == 21
    assert Solution().numOfMinutes(n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]) == 3
    assert Solution().numOfMinutes(n = 4, headID = 2, manager = [3,3,-1,2], informTime = [0,0,162,914]) == 1076
