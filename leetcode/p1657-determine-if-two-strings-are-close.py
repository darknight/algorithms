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
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        set1 = set(word1)
        set2 = set(word2)
        if set1 != set2:
            return False
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)
        for w in word1:
            cnt1[w] += 1
        for w in word2:
            cnt2[w] += 1
        list1 = sorted(list(cnt1.values()))
        list2 = sorted(list(cnt2.values()))
        return list1 == list2


if __name__ == '__main__':
    print(Solution().closeStrings("cabbba", "aabbss"))
    print(Solution().closeStrings("uau", "ssx"))
