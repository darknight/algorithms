#!/usr/bin/env python3

import math
import itertools
from collections import defaultdict
from typing import List
from typing import Set

try:
    from _tree import *
except ImportError:
    pass

try:
    from _list import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        targets = set()
        size = len(arr)
        for i in range(size):
            if arr[i] == 0:
                targets.add(i)
        if len(targets) == 0:
            return False

        marked = [False] * size
        res = [False]
        self.dfs(start, arr, marked, targets, res)

        return res[0]

    def dfs(self, idx: int, arr: List[int], marked: List[bool], targets: Set[int], res: List[bool]):
        if res[0] is True:
            return
        if idx in targets:
            res[0] = True
            return
        if marked[idx] is True:
            return
        marked[idx] = True
        if idx + arr[idx] < len(arr):
            self.dfs(idx + arr[idx], arr, marked, targets, res)
        if idx - arr[idx] >= 0:
            self.dfs(idx - arr[idx], arr, marked, targets, res)

    # TODO: bfs

if __name__ == '__main__':
    assert Solution().canReach(arr = [4,2,3,0,3,1,2], start = 5) is True
    assert Solution().canReach(arr = [4,2,3,0,3,1,2], start = 0) is True
    assert Solution().canReach(arr = [3,0,2,1,2], start = 2) is False
