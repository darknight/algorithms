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
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if len(s) == 1:
            return s == goal
        if s == goal:
            cnt = defaultdict(int)
            for c in s:
                cnt[c] += 1
                if cnt[c] >= 2:
                    return True
            return False

        diff_s = ""
        diff_goal = ""
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_s = diff_s + s[i]
                diff_goal = diff_goal + goal[i]
        if len(diff_s) != 2:
            return False
        swap = diff_s[1] + diff_s[0]

        return swap == diff_goal



if __name__ == '__main__':
    pass
