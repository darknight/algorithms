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
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])
        M = len(slots1)
        N = len(slots2)

        interset = []
        i = 0
        j = 0
        while i < M and j < N:
            s1, e1 = slots1[i][0], slots1[i][1]
            s2, e2 = slots2[j][0], slots2[j][1]
            if e1 <= s2:
                i += 1
                continue
            if e2 <= s1:
                j += 1
                continue
            interset.append([max(s1, s2), min(e1, e2)])
            if e1 < e2:
                i += 1
            elif e1 > e2:
                j += 1
            else:
                i += 1
                j += 1

        # print(interset)
        res = []
        for item in interset:
            s, e = item[0], item[1]
            if e - s >= duration:
                res = [s, s + duration]
                break
        # print(res)
        return res


if __name__ == '__main__':
    # assert Solution().minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8) == [60,68]
    assert Solution().minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 12) == []
