#!/usr/bin/env python3

import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c <= 2:
            return True
        j = int(math.sqrt(c))
        i = 0
        while i <= j:
            if i * i + j * j > c:
                j -= 1
            elif i * i + j * j < c:
                i += 1
            else:
                return True
        return False

if __name__ == '__main__':
    assert Solution().judgeSquareSum(3) == False
    assert Solution().judgeSquareSum(18) == True