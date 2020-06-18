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
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cnt = defaultdict(int)
        for ch in s:
            cnt[ch] += 1
        if len(cnt) < maxLetters:
            return 0

    def dfs(self):
        pass


if __name__ == '__main__':
    pass
