#!/usr/bin/env python3

import math, itertools, functools, heapq
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple


class Solution:
    pass


if __name__ == '__main__':
    sln = Solution()
    T = int(input())
    for i in range(1, T + 1):
        n, m = [int(s) for s in input().split(" ")]
        print("Case #{}: {} {}".format(i, n + m, n * m))
