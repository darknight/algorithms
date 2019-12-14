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
    def TLE_numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices == 0 and cheeseSlices > 0:
            return []
        if tomatoSlices > 0 and cheeseSlices == 0:
            return []
        if tomatoSlices == 0 and cheeseSlices == 0:
            return [0,0]
        if cheeseSlices >= tomatoSlices: # truncate
            return []

        res = [-1, -1]
        self.TLE_dfs(tomatoSlices, cheeseSlices, 0, 0, res)

        if res[0] == -1:
            return []
        return res

    def TLE_dfs(self, remain_t: int, remain_c: int, jumbo: int, small: int, res: List[int]):
        if res[0] > -1:
            return
        if remain_c < 0 or remain_t < 0:
            return
        if remain_c == 0 and remain_t == 0:
            res[0] = jumbo
            res[1] = small
            return
        if remain_c >= remain_t:
            return

        self.dfs(remain_t-4, remain_c-1, jumbo+1, small, res)
        self.dfs(remain_t-2, remain_c-1, jumbo, small+1, res)


    def REC_ERR_numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices == 0 and cheeseSlices > 0:
            return []
        if tomatoSlices > 0 and cheeseSlices == 0:
            return []
        if tomatoSlices == 0 and cheeseSlices == 0:
            return [0,0]
        if cheeseSlices >= tomatoSlices:
            return []

        res = [-1, -1]
        mem = set()
        self.REC_ERR_dfs(tomatoSlices, cheeseSlices, 0, 0, res, mem)

        if res[0] == -1:
            return []
        return res

    def REC_ERR_dfs(self, remain_t: int, remain_c: int, jumbo: int, small: int, res: List[int], mem):
        if (jumbo, small) in mem:
            return
        mem.add((jumbo, small))
        if res[0] > -1:
            return
        if remain_c < 0 or remain_t < 0:
            return
        if remain_c == 0 and remain_t == 0:
            res[0] = jumbo
            res[1] = small
            return
        if remain_c >= remain_t:
            return

        if (jumbo + 1, small) not in mem:
            self.dfs(remain_t-4, remain_c-1, jumbo+1, small, res, mem)
        if (jumbo, small + 1) not in mem:
            self.dfs(remain_t-2, remain_c-1, jumbo, small+1, res, mem)

    def TLE_1_numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices == 0 and cheeseSlices > 0:
            return []
        if tomatoSlices > 0 and cheeseSlices == 0:
            return []
        if tomatoSlices == 0 and cheeseSlices == 0:
            return [0,0]
        if cheeseSlices >= tomatoSlices:
            return []

        max_jumbo = min(tomatoSlices // 4, cheeseSlices)
        max_small = min(tomatoSlices // 2, cheeseSlices)

        for i in range(max_jumbo + 1):
            for j in range(max_small + 1):
                t, c = i * 4 + j * 2, i + j
                if t == tomatoSlices and c == cheeseSlices:
                    print(i, j)
                    return [i, j]
                if t > tomatoSlices or c > cheeseSlices:
                    break

        return []

    def TLE_2_numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices == 0 and cheeseSlices > 0:
            return []
        if tomatoSlices > 0 and cheeseSlices == 0:
            return []
        if tomatoSlices == 0 and cheeseSlices == 0:
            return [0,0]
        if cheeseSlices >= tomatoSlices:
            return []

        max_small = min(tomatoSlices // 2, cheeseSlices)

        dp = []
        for j in range(max_small + 1):
            t, c = 2 * j, j
            if t == tomatoSlices and c == cheeseSlices:
                return [0, j]
            dp.append([t, c])

        for j in range(max_small, -1, -1):
            remind_t = tomatoSlices - dp[j][0]
            remind_c = cheeseSlices - dp[j][1]
            max_jumbo = min(remind_t // 4, remind_c)
            for i in range(max_jumbo, -1, -1):
                t, c = 4 * i, i
                if dp[j][0] + t > tomatoSlices or dp[j][1] + c > cheeseSlices:
                    continue
                if dp[j][0] + t == tomatoSlices and dp[j][1] + c == cheeseSlices:
                    return [i, j]
                else:
                    break

        return []

    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        """
        4a + 2b == tomatoSlices
        a + b == cheeseSlices
        =>
        a = tomatoSlices / 2 - cheeseSlices
        b = 2 * cheeseSlices - tomatoSlices / 2
        """
        if tomatoSlices % 2 != 0:
            return []
        jumbo = tomatoSlices // 2 - cheeseSlices
        small = 2 * cheeseSlices - tomatoSlices // 2

        if jumbo < 0 or small < 0:
            return []

        return [jumbo, small]



if __name__ == '__main__':
    assert Solution().numOfBurgers(16, 7) == [1,6]
    assert Solution().numOfBurgers(17, 4) == []
    assert Solution().numOfBurgers(4, 17) == []
    assert Solution().numOfBurgers(0, 0) == [0, 0]
    assert Solution().numOfBurgers(2,1) == [0,1]
    assert Solution().numOfBurgers(3962, 1205) == [776, 429]
    assert Solution().numOfBurgers(19060, 5504) == [4026, 1478]
