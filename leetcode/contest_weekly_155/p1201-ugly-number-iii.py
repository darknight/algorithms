#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        """
        combinatorial mathematics: inclusion–exclusion principle
        """

        def lcm(x, y):
            return x * y // math.gcd(x, y)

        def totalBefore(k: int):
            p1 = k // a + k // b + k // c
            p2 = k // lcm(a, b) + k // lcm(b, c) + k // lcm(a, c)
            p3 = k // lcm(a, lcm(b, c))

            return p1 - p2 + p3

        if n == 1:
            return min(a, b, c)

        start = 1
        end = 2 * 10 ** 9
        while start <= end:
            m = start + (end - start) // 2
            tmp_n = totalBefore(m)
            # print(start, end, m, tmp_n)
            if tmp_n <= n - 1:
                start = m + 1
            else:
                end = m - 1

        return start



if __name__ == '__main__':
    # assert Solution().nthUglyNumber(3,2,3,5) == 4
    # assert Solution().nthUglyNumber(4,2,3,4) == 6
    # assert Solution().nthUglyNumber(5,2,11,13) == 10
    # assert Solution().nthUglyNumber(1000000000,2,217983653,336916467) == 1999999984
    assert Solution().nthUglyNumber(5,2,3,3) == 8