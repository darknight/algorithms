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
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res += self.sum_of_divisors(num)

        return res

    def sum_of_divisors(self, num: int) -> int:
        divisors = set()
        for d in range(1, int(math.sqrt(num)+1)):
            if len(divisors) > 4:
                break
            if num % d == 0:
                divisors.add(d)
                divisors.add(num // d)

        if len(divisors) == 4:
            return sum(divisors)

        return 0



if __name__ == '__main__':
    pass
