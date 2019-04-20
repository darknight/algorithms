#!/usr/bin/env python3

class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if abs(x) == 1.0:
            if n % 2 == 0:
                return abs(x)
            else:
                return x
        res = 1.0
        neg = False
        if n < 0:
            if abs(x) < 1.0:
                x = 1.0 / x
            else:
                neg = True
            n = -n
        while n:
            res *= x
            n -= 1
            if abs(res) < 1e-15:
                res = 0.0
                break
        if neg:
            res = 1.0 / res
        return res

if __name__ == '__main__':
    #NOTE: WA or RE for these cases, bloody hell...
    print(Solution().myPow(2.0, 8))
    print(Solution().myPow(34.00515, -3))
    print(Solution().myPow(0.00001, 2147483647))
    print(Solution().myPow(0.44894, -5))
    print(Solution().myPow(1.00000, 2147483647))
    print(Solution().myPow(-1.00000, -2147483648))
    print(Solution().myPow(-13.62608, 3))

