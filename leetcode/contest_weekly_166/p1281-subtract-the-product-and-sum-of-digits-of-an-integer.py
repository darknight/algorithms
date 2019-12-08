#!/usr/bin/env python3

import math
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
    def subtractProductAndSum(self, n: int) -> int:
        nums = []
        while n > 0:
            nums.append(n % 10)
            n = n // 10

        product = 1
        for num in nums:
            product *= num

        return product - sum(nums)

if __name__ == '__main__':
    assert Solution().subtractProductAndSum(234) == 15
    assert Solution().subtractProductAndSum(4421) == 21
