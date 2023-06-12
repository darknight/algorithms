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
    def maxVowels(self, s: str, k: int) -> int:
        curr = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(k):
            if s[i] in vowels:
                curr += 1
        res = curr

        for i in range(k, len(s)):
            if s[i-k] in vowels:
                curr -= 1
            if s[i] in vowels:
                curr += 1
            res = max(curr, res)

        return res


if __name__ == '__main__':
    pass
