#!/usr/bin/env python3

from typing import List
class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        res = 0
        num = 0
        for a in arr:
            if res + a > 5000:
                break
            res += a
            num += 1
        return num

if __name__ == '__main__':
    assert Solution().maxNumberOfApples([100,200,150,1000]) == 4
    assert Solution().maxNumberOfApples([900,950,800,1000,700,800]) == 5