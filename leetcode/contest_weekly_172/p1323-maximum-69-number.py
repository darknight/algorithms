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
    def maximum69Number (self, num: int) -> int:
        digits = []
        while num > 0:
            digits.insert(0, num % 10)
            num = num // 10

        for i in range(len(digits)):
            if digits[i] == 6:
                digits[i] = 9
                break
        res = 0
        for i in range(len(digits)):
            res = res * 10 + digits[i]

        return res


if __name__ == '__main__':
    pass
