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
    def WA_dieSimulator(self, n: int, rollMax: List[int]) -> int:
        """
        this is a misunderstanding of the question statement
        for example:
        n = 3, rollMax = [1,1,1,2,2,3]
        this code failed to produce [1,2,1], [1,3,1] ... [1,6,1]...
        [2,1,2]...[2,6,2]...[3,1,3]...[3,6,3]
        """
        res = [0]
        def perm(idx: int, roll: List[int], res: List[int]):
            if idx == n:
                res[0] += 1
                return
            for i in range(6):
                if roll[i] > 0:
                    roll[i] -= 1
                    perm(idx + 1, roll, res)
                    roll[i] += 1

        perm(0, rollMax, res)

        print(res)
        return res[0] % (10 ** 9 + 7)

    def TLE_dieSimulator(self, n: int, rollMax: List[int]) -> int:

        def dfs(pos: int, roll: List[int], last: int, count: int, res: List[int], tmp: List[int]):
            if pos == n:
                res[0] += 1
                print(tmp)
                return
            else:
                for i in range(6):
                    if last == i:
                        if count == roll[i]:
                            continue
                        else:
                            tmp.append(i+1)
                            dfs(pos+1, roll, last, count+1, res, tmp)
                            tmp.pop()
                    else:
                        tmp.append(i+1)
                        dfs(pos+1, roll, i, 1, res, tmp)
                        tmp.pop()

        res = [0]
        tmp = []
        dfs(0, rollMax, -1, 0, res, tmp)

        print(res)
        return res[0] % (10 ** 9 + 7)

    def TLE_SO_dieSimulator(self, n: int, rollMax: List[int]) -> int:
        """
        refer to discussion:
        https://leetcode.com/problems/dice-roll-simulation/discuss/403819/DFS-%2B-Memorization-Short-and-Simple

        but even I use memorization, locally got
        `RecursionError: maximum recursion depth exceeded in comparison`
        when submitted, I got
        `TLE`

        have to go DP
        """
        mem = []
        for _ in range(5000):
            tmp = []
            for _ in range(6):
                s = [0] * 16
                tmp.append(s)
            mem.append(tmp)

        def dfs(pos: int, roll: List[int], last: int, count: int):
            if pos == 0:
                return 1
            elif last >= 0 and mem[pos][last][count] > 0:
                return mem[pos][last][count]
            else:
                r = 0
                for i in range(6):
                    if i == last and count == roll[i]:
                        continue
                    if i == last:
                        r += dfs(pos-1, roll, i, count + 1)
                    else:
                        r += dfs(pos-1, roll, i, 1)
                if last >= 0:
                    mem[pos][last][count] = r
                return r

        res = dfs(n, rollMax, -1, 0)
        print(res)
        return res % (10 ** 9 + 7)

    def Other_dieSimulator(self, n: int, rollMax: List[int]) -> int:
        """
        This is from https://leetcode.com/problems/dice-roll-simulation/discuss/403858/Python-Simple-memoization
        locally it got `RecursionError: maximum recursion depth exceeded in comparison`
        but on website it's accepted...
        """
        def helper(currentIndex, n, rollMax, pre, d):
            if currentIndex == n:
                return 1
            elif currentIndex > n:
                return 0
            count = 0
            if (currentIndex, pre) in d:  # if this state is already calculated, return the ans
                return d[(currentIndex, pre)]
            for index in range(6):
                if index != pre:
                    for repeat in range(1, rollMax[index] + 1):
                        count += helper(currentIndex + repeat, n, rollMax, index, d)
            d[(currentIndex, pre)] = count  # save the computation
            return count

        MOD = 10 ** 9 + 7
        d = {}  # dictionary to save the states
        return helper(0, n, rollMax, -1, d) % MOD

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        """
        from: https://leetcode.com/problems/dice-roll-simulation/discuss/404840/Short-Python-DP-with-detailed-image-explanation

        dp[i][j] means how many combinations it could be that at i-th rolling and the last face is j

        dp[i][j] =
        """
        dp = []
        for _ in range(n+1):
            dp.append([0] * 6)

        # init
        for j in range(6):
            dp[1][j] = 1

        for i in range(2, n+1):
            for j in range(6):
                times = rollMax[j]
                for k in range(1, times+1):
                    if k < i:
                        for jj in range(6):
                            if jj == j:
                                continue
                            dp[i][j] += dp[i - k][jj]
                    elif k == i:
                        dp[i][j] += 1
                    else:
                        break

        return sum(dp[-1]) % 1000000007



if __name__ == '__main__':
    assert Solution().dieSimulator(2, [1,1,2,2,2,3]) == 34
    assert Solution().dieSimulator(2, [1,1,1,1,1,1]) == 30
    assert Solution().dieSimulator(3, [1,1,1,2,2,3]) == 181
    assert Solution().dieSimulator(3000, [9,3,5,10,2,5])
    assert Solution().dieSimulator(5000, [13,3,12,14,11,11])
