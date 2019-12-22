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
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if 10 <= num < 100:
                res += 1
            elif 1000 <= num < 10000:
                res += 1
            elif num == 100000:
                res += 1

        return res


if __name__ == '__main__':
    pass
