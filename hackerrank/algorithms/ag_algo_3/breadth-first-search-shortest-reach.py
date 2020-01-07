#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List, Set
from collections import defaultdict, Counter

def bfs(n: int, m: int, edges: List[List[int]], s: int):
    res = [-1] * (n+1)
    res[s] = 0
    table = []
    for _ in range(n+1):
        table.append([])
    for edge in edges:
        u, v = edge[0], edge[1]
        table[u].append(v)
        table[v].append(u)

    level = 0
    queue = [s]
    while len(queue) > 0:
        level += 1
        next_level = []
        for w in queue:
            for v in table[w]:
                if res[v] == -1:
                    res[v] = level * 6
                    next_level.append(v)
        queue = next_level

    return res[1:s] + res[s+1:]

if __name__ == '__main__':
    bfs(5, 3, [[1,2],[1,3],[3,4]], 1)
