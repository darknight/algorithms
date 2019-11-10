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
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)
        size = len(chars)
        if len(chars) == 0:
            return ""

        idx = []
        queue = []
        for i in range(size):
            if chars[i] == '(':
                queue.append(chars[i])
                idx.append(i)
            if chars[i] == ')':
                if len(queue) > 0 and queue[-1] == '(':
                    queue.pop()
                    idx.pop()
                else:
                    queue.append(chars[i])
                    idx.append(i)

        filters = set(idx)
        res = []
        for i in range(size):
            if i in filters:
                continue
            else:
                res.append(chars[i])

        # print(''.join(res))
        return ''.join(res)


if __name__ == '__main__':
    assert Solution().minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"
    assert Solution().minRemoveToMakeValid("a)b(c)d") == "ab(c)d"
    assert Solution().minRemoveToMakeValid("))((") == ""
    assert Solution().minRemoveToMakeValid("(a(b(c)d)") == "a(b(c)d)"
