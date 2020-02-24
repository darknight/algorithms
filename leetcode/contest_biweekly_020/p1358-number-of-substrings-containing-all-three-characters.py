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
    def AC_numberOfSubstrings(self, s: str) -> int:
        abc = [0, 0, 0]
        i = 0
        while i < len(s) and (abc[0] == 0 or abc[1] == 0 or abc[2] == 0):
            idx = ord(s[i]) - ord('a')
            abc[idx] += 1
            i += 1

        if abc[0] == 0 or abc[1] == 0 or abc[2] == 0:
            return 0

        j = i
        res = len(s) - j + 1

        for i in range(1, len(s)):
            last = ord(s[i-1]) - ord('a')
            abc[last] -= 1

            while j < len(s) and (abc[0] == 0 or abc[1] == 0 or abc[2] == 0):
                idx = ord(s[j]) - ord('a')
                abc[idx] += 1
                j += 1

            if abc[0] == 0 or abc[1] == 0 or abc[2] == 0:
                return res

            res += len(s) - j + 1

        return res


    def numberOfSubstrings(self, s: str) -> int:
        abc = [0, 0, 0]
        j = 0
        res = 0

        for i in range(0, len(s)):
            if i > 0:
                last = ord(s[i-1]) - ord('a')
                abc[last] -= 1

            while j < len(s) and (abc[0] == 0 or abc[1] == 0 or abc[2] == 0):
                idx = ord(s[j]) - ord('a')
                abc[idx] += 1
                j += 1

            if abc[0] == 0 or abc[1] == 0 or abc[2] == 0:
                break

            res += len(s) - j + 1

        return res



if __name__ == '__main__':
    assert Solution().numberOfSubstrings("abcabc") == 10
    assert Solution().numberOfSubstrings("aaacb") == 3
    assert Solution().numberOfSubstrings("abc") == 1
    assert Solution().numberOfSubstrings("aaa") == 0
