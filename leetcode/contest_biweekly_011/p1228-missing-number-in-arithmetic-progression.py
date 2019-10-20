#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        size = len(arr)
        diff = (arr[-1] - arr[0]) // size
        if diff == 0:
            return arr[0]
        for i in range(1, size):
            if arr[i] - arr[i-1] != diff:
                return arr[i-1] + diff


if __name__ == '__main__':
    # assert Solution().missingNumber([5,7,11,13]) == 9
    # assert Solution().missingNumber([15,13,12]) == 14
    assert Solution().missingNumber([0,0,0,0,0]) == 0
