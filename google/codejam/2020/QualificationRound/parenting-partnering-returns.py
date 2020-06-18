#!/usr/bin/env python3

import math, itertools, functools, heapq
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple


class Solution:

    def WA_assign_work(self, schedule: List[Tuple[int, ...]], N: int) -> str:
        intervals = sorted(schedule)
        alloc = {}

        j_avail_after = 0
        c_avail_after = 0

        for i in range(N):
            start, end = intervals[i]
            if start >= j_avail_after:
                alloc[intervals[i]] = 'J'
                j_avail_after = end
            elif start >= c_avail_after:
                alloc[intervals[i]] = 'C'
                c_avail_after = end
            else:
                return 'IMPOSSIBLE'

        res = ''.join([alloc[item] for item in schedule])
        return res


    def WA_2_assign_work(self, schedule: List[Tuple[int, ...]], N: int) -> str:
        intervals = sorted(schedule, key=lambda x: (x[1], x[0]))
        alloc = {}

        prev = intervals[0]
        alloc[prev] = 'C'

        j_avail_after = 0
        c_avail_after = prev[1]

        for i in range(1, N):
            curr = intervals[i]
            if curr[0] >= prev[1]:
                if alloc[prev] == 'C':
                    alloc[curr] = 'C'
                    c_avail_after = curr[1]
                else:
                    alloc[curr] = 'J'
                    j_avail_after = curr[1]
                prev = curr
            else:
                if alloc[prev] == 'C':
                    if curr[0] >= j_avail_after:
                        alloc[curr] = 'J'
                    else:
                        return 'IMPOSSIBLE'
                else:
                    if curr[0] >= c_avail_after:
                        alloc[curr] = 'C'
                    else:
                        return 'IMPOSSIBLE'
                prev = curr


        res = ''.join([alloc[item] for item in schedule])
        return res


    def WA_2_assign_work(self, schedule: List[Tuple[int, ...]], N: int) -> str:
        pass




if __name__ == '__main__':
    sln = Solution()
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        intervals = [tuple(map(int, input().split())) for _ in range(N)]
        res = sln.assign_work(intervals, N)
        print("Case #{}: {}".format(i, res))
