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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        total_edge = len(connections)
        if total_edge < n - 1:
            return -1
        table = [-1] * n
        for conn in connections:
            u, v = conn[0], conn[1]
            self.union(u, v, table)

        num = 0
        for i in range(n):
            if table[i] == -1:
                num += 1

        return num - 1

    def union(self, node1: int, node2: int, table: List[int]):
        root1 = self.find(node1, table)
        root2 = self.find(node2, table)
        if root1 != root2:
            table[root2] = root1

    def find(self, node: int, table: List[int]) -> int:
        if table[node] == -1:
            return node
        table[node] = self.find(table[node], table)
        return table[node]



if __name__ == '__main__':
    pass
