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
    def TLE_closestDivisors(self, num: int) -> List[int]:
        if num == 1:
            return [1, 2]
        a = 0
        b = math.inf

        start = int(math.sqrt(num + 2)) + 1
        for x in range(start, 1, -1):
            low = x
            high = num + 2
            while low <= high: # must include `=`
                mid = low + (high - low) // 2
                target = x * mid
                if target == num + 1 or target == num + 2:
                    if abs(x - mid) < abs(a - b):
                        a = x
                        b = mid
                    break
                elif target < num + 1:
                    low = mid + 1
                else:
                    high = mid - 1

        return [a, b]



    def closestDivisors(self, num: int) -> List[int]:
        """
        refer to
        https://leetcode.com/problems/closest-divisors/discuss/517962/Greedy-beat-100-time-memory

        similar idea
        https://leetcode.com/problems/closest-divisors/discuss/517567/C%2B%2B-Smart-Brute-Force
        """
        for i in reversed(range(1, int(math.sqrt(num + 2)) + 1)):
            if (num + 1) % i == 0:
                return [i, (num + 1) // i]
            if (num + 2) % i == 0:
                return [i, (num + 2) // i]



if __name__ == '__main__':
    print(Solution().closestDivisors(8))
    print(Solution().closestDivisors(123))
    print(Solution().closestDivisors(999))
    print(Solution().closestDivisors(524675377))
    print(Solution().closestDivisors(688427155))
    print(Solution().closestDivisors(501284630))
