#!/usr/bin/env python3

import math, itertools, functools, heapq
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass


class Solution:
    def TLE_tupleSameProduct(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        nums.sort()
        res = 0
        for i in range(len(nums)-4+1):
            a = nums[i]
            b = a+1
            c = a+2
            d = a+3
            if a * c < b * d and a * d > b * c:
                break
            for j in range(i+1, len(nums)-3+1):
                b = nums[j]
                c = b+1
                d = b+2
                if a * c < b * d and a * d > b * c:
                    break
                for k in range(j+1, len(nums)-2+1):
                    c = nums[k]
                    d = c+1
                    if a * c < b * d and a * d > b * c:
                        break
                    for p in range(k+1, len(nums)-1+1):
                        d = nums[p]
                        if a * c == b * d or a * d == b * c:
                            res += 1

        return res * 8


    def tupleSameProduct(self, nums: List[int]) -> int:
        nums.sort()
        products = defaultdict(int)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                products[nums[i] * nums[j]] += 1
        res = 0
        for _, v in products.items():
            if v == 1:
                continue
            res += v * (v -1) // 2

        return res * 8


if __name__ == '__main__':
    print(Solution().tupleSameProduct([2,3,4,6]))
    print(Solution().tupleSameProduct([1,2,4,5,10]))
    print(Solution().tupleSameProduct([2,3,4,6,8,12]))
    print(Solution().tupleSameProduct([2,3,5,7]))
    print(Solution().tupleSameProduct([i for i in range(1,1000)]))
