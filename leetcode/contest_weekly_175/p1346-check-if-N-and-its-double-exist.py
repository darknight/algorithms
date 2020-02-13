#!/usr/bin/env python3

import math, itertools, functools
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        m = defaultdict(int)
        zeros = 0
        for i, val in enumerate(arr):
            if val == 0:
                zeros += 1
            else:
                m[val] = i
        if zeros > 1:
            return True
        for val in arr:
            if 2 * val in m:
                return True

        return False


if __name__ == '__main__':
    pass
