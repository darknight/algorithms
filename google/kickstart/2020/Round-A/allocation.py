#!/usr/bin/env python3

import math, itertools, functools, heapq
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple


class Solution:
    def buy(self, N: int, B: int, costs: List[int]) -> int:
        costs.sort()
        res = 0
        for c in costs:
            if c <= B:
                B -= c
                res += 1
            else:
                break

        return res


if __name__ == '__main__':
    sln = Solution()
    T = int(input())
    for i in range(1, T + 1):
        N, B = [int(s) for s in input().split(" ")]
        costs = [int(c) for c in input().split(" ")]
        res = sln.buy(N, B, costs)
        print("Case #{}: {}".format(i, res))
