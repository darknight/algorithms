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

    # TODO: not elegant, check discussion
    def maximumTime(self, time: str) -> str:
        h, m = time.split(":", 2)
        hour = ''
        if h == '??':
            hour = '23'
        elif h[0] == '?' and h[1] > '3':
            hour = '1' + h[1]
        elif h[0] == '?' and h[1] <= '3':
            hour = '2' + h[1]
        elif h[0] == '2' and h[1] == '?':
            hour = '23'
        elif h[0] < '2' and h[1] == '?':
            hour = h[0] + '9'
        else:
            hour = h

        minute = ''
        if m == '??':
            minute = '59'
        elif m[0] == '?':
            minute = '5' + m[1]
        elif m[1] == '?':
            minute = m[0] + '9'
        else:
            minute = m

        return ":".join([hour, minute])


if __name__ == '__main__':
    print(Solution().maximumTime("2?:?0"))
    print(Solution().maximumTime("00:00"))
    print(Solution().maximumTime("??:??"))
    print(Solution().maximumTime("0?:3?"))
    print(Solution().maximumTime("1?:22"))
