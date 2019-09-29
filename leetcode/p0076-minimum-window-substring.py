#!/usr/bin/env python3
from collections import defaultdict
import math

class Solution:
    from typing import List

    def minWindow(self, s: str, t: str) -> str:
        """
        sliding window
        checked answer
        """
        if len(s) == 0:
            return ""
        stat = defaultdict(int)
        for c in t:
            stat[c] += 1

        start = 0
        end = 0
        count = len(t)
        res = ""
        min_size = math.inf
        while end < len(s):
            if s[end] in t:
                if stat[s[end]] > 0:
                    count -= 1
                stat[s[end]] -= 1
            end += 1

            while count == 0:
                if end - start < min_size:
                    res = s[start:end]
                    min_size = len(res)
                if s[start] in t:
                    stat[s[start]] += 1
                    if stat[s[start]] > 0:
                        count += 1
                start += 1

        return res


if __name__ == '__main__':
    # assert Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC"
    # assert Solution().minWindow("a", "a") == "a"
    # assert Solution().minWindow("a", "b") == ""
    # assert Solution().minWindow("aa", "aa") == "aa"
    # assert Solution().minWindow("bba", "ab") == "ba"
    assert Solution().minWindow("cabwefgewcwaefgcf", "cae") == "cwae"
