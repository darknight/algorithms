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
    def printVertically(self, s: str) -> List[str]:
        words = s.split(' ')
        max_col = len(words)
        max_row = max([len(word) for word in words])

        bucket = []
        for _ in range(max_row):
            bucket.append([' '] * max_col)

        for j in range(max_col):
            word = words[j]
            for i in range(len(word)):
                bucket[i][j] = word[i]

        res = []
        for i in range(max_row):
            row = ''.join(bucket[i])
            res.append(row.rstrip())

        # print(res)
        return res

if __name__ == '__main__':
    Solution().printVertically("HOW ARE YOU")
    Solution().printVertically("TO BE OR NOT TO BE")
    Solution().printVertically("CONTEST IS COMING")
    Solution().printVertically("CONTEST")
    Solution().printVertically("HELLO W")
    Solution().printVertically("H WORLD")
