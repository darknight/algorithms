#!/usr/bin/env python3

class Solution(object):
    from typing import List
    def numberOfArithmeticSlices1(self, A: List[int]) -> int:
        """
        f(n) = (n-1)*(n-2)/2
        """
        if len(A) < 3:
            return 0
        i = 0
        j = 1
        res = 0
        for k in range(2, len(A)):
            if A[k] - A[j] == A[j] - A[j-1]:
                j = k
                continue
            else:
                n = j - i + 1
                res += (n-1)*(n-2)//2
                i = j
                j = k
        n = j - i + 1
        res += (n - 1) * (n - 2) // 2

        return res

    #TODO: use dp
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        pass

if __name__ == '__main__':
    assert Solution().numberOfArithmeticSlices([1, 2, 3, 4]) == 3
    assert Solution().numberOfArithmeticSlices([1, 1, 2, 5, 7]) == 0
