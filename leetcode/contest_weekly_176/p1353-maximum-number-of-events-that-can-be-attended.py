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
    def AC_1_maxEvents(self, events: List[List[int]]) -> int:
        """
        refer to
        https://www.youtube.com/watch?v=NjF9JGDGxg8
        """
        events.sort(key=lambda x: (x[1], x[0]))
        size = len(events)
        if size == 1:
            return 1

        seen = [0] * 100001
        res = 0
        for e in events:
            for i in range(e[0], e[1]+1):
                if seen[i] == 1:
                    continue
                seen[i] = 1
                res += 1
                break

        return res


    def AC_2_maxEvents(self, events: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/discuss/510263/JavaC%2B%2BPython-Priority-Queue
        """
        events.sort(key=lambda x: (x[0], x[1]))
        size = len(events)
        if size == 1:
            return 1

        i = 0
        pq = []
        res = 0
        for d in range(1, 100001):
            while len(pq) > 0 and pq[0] < d:
                heapq.heappop(pq)
            while i < len(events) and events[i][0] == d:
                heapq.heappush(pq, events[i][1])
                i += 1
            if len(pq) > 0:
                heapq.heappop(pq)
                res += 1

        return res


if __name__ == '__main__':
    assert Solution().maxEvents([[1,2],[2,3],[3,4],[1,2]]) == 4
