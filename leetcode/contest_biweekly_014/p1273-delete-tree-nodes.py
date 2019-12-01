#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass


class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        table = {}
        for i in range(nodes):
            if i not in table:
                table[i] = []
            p = parent[i]
            if p in table:
                table[p].append(i)
            else:
                table[p] = [i]

        root = table[-1][0]
        self.accumulate(root, table, value)

        for i in range(nodes):
            if value[i] == 0:
                self.delete_from_table(i, table)

        return len(table) - 1

    def accumulate(self, node, table, value):
        for child in table[node]:
            value[node] += self.accumulate(child, table, value)
        return value[node]

    def delete_from_table(self, i, table):
        if i not in table:
            return
        for j in table[i]:
            self.delete_from_table(j, table)
        del table[i]


if __name__ == '__main__':
    assert Solution().deleteTreeNodes(nodes = 7,
                                      parent = [-1,0,0,1,2,2,2],
                                      value = [1,-2,4,0,-2,-1,-1]) == 2
