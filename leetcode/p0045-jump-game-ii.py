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
    def jump(self, nums: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=G88X89Eo2C0

        implicit bfs, refer to
        https://leetcode.com/problems/jump-game-ii/discuss/18014/Concise-O(n)-one-loop-JAVA-solution-based-on-Greedy
        """
        res = 0
        last_furthest = 0
        curr_furthest = 0
        for i in range(len(nums)):
            if i > last_furthest:
                res += 1
                last_furthest = curr_furthest
            curr_furthest = max(curr_furthest, nums[i] + i)

        return res



if __name__ == '__main__':
    pass
