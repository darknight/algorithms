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
    from _list import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass


class Solution:
    def __init__(self):
        self.no_change = {0,1,8}
        self.change = {2,5,6,9}
        self.invalid = {3,4,7}

    def rotatedDigits(self, N: int) -> int:
        res = []
        for num in range(1, N+1):
            if self.good_num(num):
                res.append(num)

        return len(res)

    def good_num(self, num: int) -> int:
        good = False
        while num > 0:
            digit = num % 10
            if digit in self.invalid:
                good = False
                break
            elif digit in self.change:
                good = True
            num = num // 10

        return good

if __name__ == '__main__':
    assert Solution().rotatedDigits(10000)
