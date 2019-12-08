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
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start = 1
        end = 10 ** 6

        while start <= end:
            div = start + (end - start) // 2
            s = self.divide_sum(nums, div)
            # This cause WA...
            # if s == threshold:
            #     return div
            if s <= threshold:
                end = div - 1
            else:
                start = div + 1
        return start

    def divide_sum(self, nums: List[int], divisor: int) -> int:
        res = []
        for num in nums:
            res.append(math.ceil(num / divisor))
        return sum(res)


if __name__ == '__main__':
    assert Solution().smallestDivisor(nums = [1,2,5,9], threshold = 6) == 5
    assert Solution().smallestDivisor(nums = [2,3,5,7,11], threshold = 11) == 3
    assert Solution().smallestDivisor(nums = [19], threshold = 5) == 4
    assert Solution().smallestDivisor([962551,933661,905225,923035,990560],10) == 495280