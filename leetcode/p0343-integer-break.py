#!/usr/bin/env python3

class Solution(object):
    from typing import List
    def integerBreak1(self, n: int) -> int:
        """
        f(n) = max[i*(n-i), i*f(n-i)] i = 1..n-1
        will TLE if not optimising
        """
        if n <= 2:
            return 1
        res = []
        for i in range(1, n):
            res.append(max(i*(n-i), i*self.integerBreak(n-i)))

        return max(res)

    def integerBreak1(self, n: int) -> int:
        cache = [0,1,1] # f(0) is sentinel, f(1) == 1, f(2) == 2
        if n <= 2:
            return 1
        for t in range(3, n+1):
            res = []
            for i in range(1, t):
                res.append(max(i*(t-i), i*cache[t-i]))
            cache.append(max(res))
        return cache[-1]

    def integerBreak(self, n: int) -> int:
        cache = [0,1,1]
        if n <= 2:
            return 1
        for t in range(3, n+1):
            res = 1
            for i in range(1, t):
                res = max(res, max(i*(t-i), i*cache[t-i]))
            cache.append(res)
        return cache[-1]

if __name__ == '__main__':
    assert Solution().integerBreak(2) == 1
    assert Solution().integerBreak(10) == 36
    assert Solution().integerBreak(7) == 12
    assert Solution().integerBreak(5) == 6