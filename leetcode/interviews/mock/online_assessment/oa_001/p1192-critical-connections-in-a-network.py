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
    def TLE_criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """try union find"""

        def union(connections: List[List[int]], marked: List[int]):
            for conn in connections:
                i, j = conn[0], conn[1]
                rooti = find(i, marked)
                rootj = find(j, marked)
                if rooti != rootj:
                    marked[rootj] = rooti

        def find(idx: int, marked: List[int]):
            if marked[idx] == -1:
                return idx
            marked[idx] = find(marked[idx], marked)
            return marked[idx]

        def connect_count(marked: List[int]) -> int:
            res = 0
            for v in marked:
                if v == -1:
                    res += 1
            return res

        size = len(connections)
        if size == 0:
            return []

        res = []
        for i in range(size):
            head = connections.pop(0)
            marked = [-1] * n
            union(connections, marked)
            if connect_count(marked) > 1:
                res.append(head)
            connections.append(head)

        return res

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        https://www.cnblogs.com/nullzx/p/7968110.html
        https://www.byvoid.com/zhs/blog/scc-tarjan
        """
        res = []
        return res



if __name__ == '__main__':
    assert Solution().criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]) == [[1,3]]
