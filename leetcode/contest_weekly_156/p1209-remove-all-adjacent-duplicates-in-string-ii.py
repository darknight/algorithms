#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) < k:
            return s
        pattern = [chr(ord('a') + i) * k for i in range(26)]

        replaced = True
        while replaced:
            replaced = False
            for p in pattern:
                ss = s.replace(p, '')
                if len(ss) < len(s):
                    replaced = True
                    s = ss

        return s


if __name__ == '__main__':
    assert Solution().removeDuplicates("abcd", 2) == "abcd"
    assert Solution().removeDuplicates("deeedbbcccbdaa", 3) == "aa"
    assert Solution().removeDuplicates("pbbcggttciiippooaais", 2) == "ps"
