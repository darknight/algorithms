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
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        size = len(nums)
        if size % k != 0:
            return False
        if k == 1:
            return True
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1

        keys = sorted(cnt.keys())
        res = True
        while len(keys) > 0 and res:
            head = keys[0]
            if cnt[head] == 0:
                keys.pop(0)
                continue
            for i in range(k):
                cnt[head+i] -= 1
                if cnt[head+i] < 0:
                    res = False
                    break

        return res



if __name__ == '__main__':
    assert Solution().isPossibleDivide(nums = [1,2,3,3,4,4,5,6], k = 4) is True
    assert Solution().isPossibleDivide(nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3) is True
    assert Solution().isPossibleDivide(nums = [3,3,2,2,1,1], k = 3) is True
    assert Solution().isPossibleDivide(nums = [1,2,3,4], k = 3) is False
