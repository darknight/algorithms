#!/usr/bin/env python3

class Solution(object):
    from typing import List
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        if x == 2 or x == 3:
            return 1
        l = 2
        h = x
        while l <= h:
            m = l + (h - l) // 2
            if m * m == x:
                return m
            elif m * m > x:
                h = m - 1
            elif m * m < x:
                l = m + 1
        return h


if __name__ == '__main__':
    assert Solution().mySqrt(4) == 2
    assert Solution().mySqrt(8) == 2
    assert Solution().mySqrt(10) == 3
    assert Solution().mySqrt(15) == 3