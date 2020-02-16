#!/usr/bin/env python3

import math, itertools, functools
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass

class Solution:
    def TLE_minJumps(self, arr: List[int]) -> int:
        """
        refer to
        https://leetcode.com/problems/jump-game-iv/discuss/504143/C-Solution-with-Comments-and-Explanation

        """
        size = len(arr)
        if size == 1:
            return 0
        if size == 2:
            return 1

        same_val = defaultdict(list)
        for i, v in enumerate(arr):
            same_val[v].append(i)

        marked = [False] * size
        marked[0] = True
        queue = [0]
        res = 0
        while len(queue) > 0:
            tmp = []
            for curr in queue:
                if curr == size - 1:
                    return res
                else:
                    if curr - 1 >= 0 and marked[curr-1] is False:
                        marked[curr-1] = True
                        tmp.append(curr-1)
                    if curr + 1 < size and marked[curr+1] is False:
                        marked[curr+1] = True
                        tmp.append(curr+1)
                    for idx in same_val[arr[curr]]:
                        if marked[idx] is False:
                            marked[idx] = True
                            tmp.append(idx)
            queue = tmp
            res += 1

    def minJumps(self, arr: List[int]) -> int:
        """
        refer to
        https://leetcode.com/problems/jump-game-iv/discuss/504143/C-Solution-with-Comments-and-Explanation
        """
        size = len(arr)
        if size == 1:
            return 0
        if size == 2:
            return 1

        same_val = defaultdict(list)
        for i, v in enumerate(arr):
            same_val[v].append(i)

        marked = [False] * size
        marked[0] = True
        queue = [0]
        res = 0
        while len(queue) > 0:
            tmp = []
            for curr in queue:
                if curr == size - 1:
                    return res
                else:
                    if curr - 1 >= 0 and marked[curr-1] is False:
                        marked[curr-1] = True
                        tmp.append(curr-1)
                    if curr + 1 < size and marked[curr+1] is False:
                        marked[curr+1] = True
                        tmp.append(curr+1)
                    for idx in same_val[arr[curr]]:
                        if marked[idx] is False:
                            marked[idx] = True
                            tmp.append(idx)
                    # to avoid query same_val again
                    same_val[arr[curr]].clear()
            queue = tmp
            res += 1

        return res


if __name__ == '__main__':
    assert Solution().minJumps([100,-23,-23,404,100,23,23,23,3,404]) == 3
