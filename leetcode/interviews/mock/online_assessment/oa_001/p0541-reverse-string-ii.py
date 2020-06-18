#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass


class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        def reverse(ss: str) -> str:
            size = len(ss)
            if size <= 1:
                return ss
            chars = list(ss)
            for i in range(size//2):
                chars[i], chars[size-1-i] = chars[size-1-i], chars[i]
            return ''.join(chars)

        split = []
        while len(s) > 0:
            tmp = s[:k]
            split.append(tmp)
            s = s[k:]

        for i in range(0, len(split), 2):
            split[i] = reverse(split[i])

        return ''.join(split)




if __name__ == '__main__':
    assert Solution().reverseStr('abcdefg', 2) == 'bacdfeg'
