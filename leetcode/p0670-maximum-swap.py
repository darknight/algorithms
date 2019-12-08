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
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num

        nums = []
        while num > 0:
            nums.insert(0, num % 10)
            num = num // 10

        size = len(nums)
        for i in range(size - 1):
            max_idx = i
            for j in range(i + 1, size):
                if nums[j] >= nums[max_idx]:
                    max_idx = j
            if nums[i] < nums[max_idx]:
                nums[i], nums[max_idx] = nums[max_idx], nums[i]
                break

        res = 0
        for n in nums:
            res = res * 10 + n

        return res


if __name__ == '__main__':
    assert Solution().maximumSwap(2736) == 7236
    assert Solution().maximumSwap(9973) == 9973
    assert Solution().maximumSwap(7539) == 9537
    assert Solution().maximumSwap(98368) == 98863
    assert Solution().maximumSwap(1993) == 9913
