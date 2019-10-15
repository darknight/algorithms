#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass


class Solution:

    def divisor(self, K) -> List[int]:
        res = [1]
        for k in range(2, K // 2 + 1):
            if K % k == 0:
                res.append(k)
        return res

    def divisorGame(self, N: int) -> bool:
        """
        define f(i) as when Alice goes first, if she can win
        TODO:
        1. use math.sqrt wrongly
        2. `n` forgot minus `d`
        3. took quite long time
        4. slow
        5. got 4 WA...
        """
        if N == 1:
            return False
        if N == 2:
            return True
        if N == 3:
            return False
        res = [0] * (N + 1)
        res[2] = 1
        res[4] = 1

        for n in range(5, N+1):
            for d in self.divisor(n):
                if res[n-d] == 0:
                    res[n] = 1
                    break

        # print(res)
        return res[N] == 1


if __name__ == '__main__':
    assert Solution().divisorGame(2) is True
    assert Solution().divisorGame(3) is False
    assert Solution().divisorGame(4) is True
    assert Solution().divisorGame(5) is False
    assert Solution().divisorGame(6) is True
    assert Solution().divisorGame(7) is False
    assert Solution().divisorGame(8) is True
