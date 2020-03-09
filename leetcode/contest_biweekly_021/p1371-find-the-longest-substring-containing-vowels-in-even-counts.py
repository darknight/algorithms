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
    def WA_findTheLongestSubstring(self, s: str) -> int:
        res = 0
        chars = list(s)
        for start in range(len(s)-1):
            if len(s) - start < res:
                break
            stat = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
            if chars[start] in stat:
                stat[chars[start]] += 1
            for end in range(start+1, len(s)):
                if chars[end] in stat:
                    stat[chars[end]] += 1
                if all(v % 2 == 0 for v in stat.values()):
                    res = max(res, end - start + 1)
        return res

    def findTheLongestSubstring(self, s: str) -> int:
        """refer to
        https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/discuss/531850/Python-solution-in-O(n)-time-and-O(1)-space-explained
        """
        bits = {'a': 16, 'e': 8, 'i': 4, 'o': 2, 'u': 1}
        val_to_idx = {0: -1}
        res = 0
        val = 0
        for i in range(len(s)):
            if s[i] in bits:
                val = val ^ bits[s[i]]
            if val not in val_to_idx:
                val_to_idx[val] = i
            else:
                res = max(res, i - val_to_idx[val])

        return res


if __name__ == '__main__':
    assert Solution().findTheLongestSubstring("eleetminicoworoep") == 13
    assert Solution().findTheLongestSubstring("leetcodeisgreat") == 5
    assert Solution().findTheLongestSubstring("bcbcbc") == 6
    assert Solution().findTheLongestSubstring("id") == 1
