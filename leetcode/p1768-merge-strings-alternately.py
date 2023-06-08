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
    def mergeAlternately(self, word1: str, word2: str) -> str:
        suffix = ""
        m = len(word1)
        n = len(word2)
        if m > n:
            suffix = word1[n:]
            word1 = word1[:n]
        elif m < n:
            suffix = word2[m:]
            word2 = word2[:m]

        res = []
        for i in range(len(word1)):
            res.append(word1[i])
            res.append(word2[i])

        return "".join(res) + suffix

    def mergeAlternately_official(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        res = []
        while i < m or j < n:
            if i < m:
                res.append(word1[i])
                i += 1
            if j < n:
                res.append(word2[j])
                j += 1

        return "".join(res)


if __name__ == '__main__':
    pass
