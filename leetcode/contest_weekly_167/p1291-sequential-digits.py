#!/usr/bin/env python3

import math
import itertools
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        lowdi = []
        num = low
        while num > 0:
            lowdi.append(num % 10)
            num = num // 10

        highdi = []
        num = high
        while num > 0:
            highdi.append(num % 10)
            num = num // 10

        res = []
        lowsize = len(lowdi)
        highsize = len(highdi)
        for n in range(lowsize, highsize+1):
            for start in range(1, 10 - n + 1):
                tmp = 0
                for i in range(n):
                    tmp = tmp * 10 + (start + i)
                if low <= tmp <= high:
                    res.append(tmp)

        print(res)
        return res

if __name__ == '__main__':
    assert Solution().sequentialDigits(low = 100, high = 300) == [123,234]
    assert Solution().sequentialDigits(low = 1000, high = 13000) == [1234,2345,3456,4567,5678,6789,12345]
    Solution().sequentialDigits(low = 1000, high = 13000000)
