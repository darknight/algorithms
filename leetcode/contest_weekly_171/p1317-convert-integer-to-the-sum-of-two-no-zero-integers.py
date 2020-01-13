#!/usr/bin/env python3

import math, itertools
from collections import defaultdict, Counter
from typing import List, Set
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        size = n // 2
        for a in range(1, size+1):
            b = n - a
            if self.has_zero(a) or self.has_zero(b):
                continue
            return [a, b]

    def has_zero(self, num: int) -> bool:
        while num > 0:
            if num % 10 == 0:
                return True
            num = num // 10
        return False


if __name__ == '__main__':
    pass
