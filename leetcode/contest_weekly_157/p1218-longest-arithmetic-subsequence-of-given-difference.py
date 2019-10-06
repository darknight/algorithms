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
    def TLE_longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = [1] * len(arr)
        for i in range(1, len(arr)):
            k = i - 1
            while k >= 0:
                if arr[i] - arr[k] == difference:
                    break
                k -= 1
            if k >= 0:
                dp[i] = max(dp[i], dp[k] + 1)

        return max(dp)

    def MY_longestSubsequence(self, arr: List[int], difference: int) -> int:

        dp = [1] * len(arr)
        cache = defaultdict(list)
        for i in range(len(arr)):
            cache[arr[i]].append(i)
        print(cache)
        for i in range(1, len(arr)):
            k = arr[i] - difference
            if k in cache:
                for idx in cache[k]:
                    if idx < i:
                        dp[i] = max(dp[i], dp[idx] + 1)

        print(dp)
        return max(dp)

    def AC1_longestSubsequence(self, arr: List[int], difference: int) -> int:

        tmp = defaultdict(int)
        for i in range(len(arr)):
            tmp[arr[i]] = tmp[arr[i]-difference] + 1

        return max(tmp.values())

    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        dp = [1] * len(arr)
        tmp = defaultdict(int)
        for i in range(len(arr) - 1, -1, -1):
            dp[i] = max(dp[i], tmp[arr[i] + difference] + 1)
            tmp[arr[i]] = dp[i]

        # print(dp)
        return max(dp)


if __name__ == '__main__':
    assert Solution().longestSubsequence([1,2,3,4], 1) == 4
    assert Solution().longestSubsequence([1,3,5,7], 1) == 1
    assert Solution().longestSubsequence([1,5,7,8,5,3,4,2,1], -2) == 4
    assert Solution().longestSubsequence([4,12,10,0,-2,7,-8,9,-9,-12,-12,8,8], 0) == 2
