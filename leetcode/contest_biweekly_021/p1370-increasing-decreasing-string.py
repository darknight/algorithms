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
    def sortString(self, s: str) -> str:
        cnt = [0] * 26
        for c in list(s):
            idx = ord(c) - ord('a')
            cnt[idx] += 1

        res = []
        while len(res) < len(s):
            for i in range(26):
                if cnt[i] > 0:
                    cnt[i] -= 1
                    res.append(chr(ord('a')+i))
            for j in range(25, -1, -1):
                if cnt[j] > 0:
                    cnt[j] -= 1
                    res.append(chr(ord('a') + j))

        return ''.join(res)




if __name__ == '__main__':
    pass
