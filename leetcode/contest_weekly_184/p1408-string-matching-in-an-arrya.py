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
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        res = []
        for i in range(len(words)-1):
            target = words[i]
            for j in range(i+1, len(words)):
                if words[j].find(target) != -1:
                    res.append(target)
                    break

        return res


if __name__ == '__main__':
    print(Solution().stringMatching(["leetcoder","leetcode","od","hamlet","am"]))
