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
    def TLE_treeDiameter(self, edges: List[List[int]]) -> int:
        size = len(edges)
        if size <= 1:
            return size

        res = defaultdict(int)
        table = defaultdict(list)

        for e in edges:
            u, v = e[0], e[1]
            table[u].append(v)
            table[v].append(u)

        for v in table.keys():
            marked = [0] * (size + 1)
            self.TLE_bfs(v, 0, [v], table, marked, res)

        return max(res.values()) - 1

    def TLE_bfs(self, v, path, queue, table, marked, res):
        if len(queue) == 0:
            res[v] = path
            return

        next_q = []
        while len(queue) > 0:
            u = queue.pop(0)
            marked[u] = 1

            for vv in table[u]:
                if marked[vv] == 0:
                    next_q.append(vv)

        self.TLE_bfs(v, path + 1, next_q, table, marked, res)

    def treeDiameter(self, edges: List[List[int]]) -> int:
        """
        refer to p0543
        """
        size = len(edges)
        if size <= 1:
            return size

        table = defaultdict(list)

        for e in edges:
            u, v = e[0], e[1]
            table[u].append(v)
            table[v].append(u)

        start = edges[0][0]
        res = [[]]
        self.dfs(start, [], res, table, [0] * len(table))
        print(res)

        start = res[0][-1]
        res = [[]]
        self.dfs(start, [], res, table, [0] * len(table))
        print(res)

        return len(res[0]) - 1


    def dfs(self, v: int, curr: List[int], res: List[List[int]], table, marked: List[int]):
        marked[v] = 1
        curr.append(v)

        for vv in table[v]:
            if marked[vv] == 0:
                self.dfs(vv, curr, res, table, marked)

        if len(curr) > len(res[0]):
            res[0] = curr.copy()
        curr.pop()


if __name__ == '__main__':
    assert Solution().treeDiameter([[0,1],[0,2]]) == 2
    assert Solution().treeDiameter([[0,1],[1,2],[2,3],[1,4],[4,5]]) == 4
