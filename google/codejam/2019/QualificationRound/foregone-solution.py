#!/usr/bin/env python3

import math, itertools, functools, heapq
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple


class Solution:

    def get_digit(self, n: int) -> Tuple[int, int]:
        al = []
        bl = []
        while n > 0:
            r = n % 10
            if r == 4:
                al.insert(0, 2)
                bl.insert(0, 2)
            else:
                al.insert(0, r)
                bl.insert(0, 0)

            n = n // 10

        a, b = 0, 0
        for i in range(len(al)):
            a = a * 10 + al[i]
            b = b * 10 + bl[i]

        return a, b


if __name__ == '__main__':
    s = Solution()
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        (a, b) = s.get_digit(N)
        print("Case #{}: {} {}".format(i, a, b))
