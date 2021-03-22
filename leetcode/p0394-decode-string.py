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
    def decodeString(self, s: str) -> str:

        def decode(t: str) -> str:
            if len(t) <= 3:
                return t
            left = mid = ""
            i = 0
            cnt = 0
            stack = []
            while i < len(t) and t[i].isalpha():
                left += t[i]
                i += 1
            if i == len(t):
                return t
            while t[i].isdigit():
                cnt = cnt * 10 + int(t[i])
                i += 1
            stack.append(t[i])
            j = i + 1
            mid = ""
            while j < len(t):
                if t[j] == "[":
                    stack.append(t[j])
                elif t[j] == "]":
                    stack.pop()
                    if len(stack) == 0:
                        break
                mid += t[j]
                j += 1

            right = t[j+1:]
            # print(left, cnt, mid, right)
            return left + decode(mid) * cnt + decode(right)

        return decode(s)


if __name__ == '__main__':
    print(Solution().decodeString("3[a]2[bc]"))
    print(Solution().decodeString("3[a2[c]]"))
    print(Solution().decodeString("2[abc]3[cd]ef"))
    print(Solution().decodeString("abc3[cd]xyz"))
    print(Solution().decodeString("leetcode"))
