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
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        stack = []
        size = len(s)
        if size <= 1:
            return 0
        stack.append(s[0])

        for i in range(1, size):
            curr = s[i]
            if len(stack) == 0:
                stack.append(curr)
            else:
                if stack[-1] != curr:
                    stack.pop()
                    if len(stack) == 0:
                        res += 1
                else:
                    stack.append(curr)

        # print(res)
        return res


if __name__ == '__main__':
    assert Solution().balancedStringSplit("RLRRLLRLRL") == 4
    assert Solution().balancedStringSplit("RLLLLRRRLR") == 3
    assert Solution().balancedStringSplit("LLLLRRRR") == 1
