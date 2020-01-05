#!/usr/bin/env python3

import math, itertools
from collections import defaultdict, Counter
from typing import List, Set
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass

class Solution:
    def WA_minInsertions(self, s: str) -> int:
        """
        from left to right, move the pointer,
        and calculate the difference, track the minimum one
        """
        left = [0] * 26
        right = [0] * 26
        char_idx = [ord(ch) - ord('a') for ch in list(s)]
        for idx in char_idx:
            right[idx] += 1

        steps = sum(right)
        size = len(char_idx)
        for i in range(size):
            idx = char_idx[i]
            # idx as pivot
            right[idx] -= 1
            s1 = self.calc_diff(left, right)
            # move idx to left
            left[idx] += 1
            s2 = self.calc_diff(left, right)
            # track the minimum
            steps = min(steps, s1, s2)

        return steps

    def calc_diff(self, left: List[int], right: List[int]) -> int:
        res = 0
        for i in range(26):
            res += abs(left[i] - right[i])
        return res

    def minInsertions(self, s: str) -> int:
        """
        refer to
        https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/discuss/470706/JavaC%2B%2BPython-Longest-Common-Sequence
        """
        rs = ''.join(reversed(s))
        lcs_len = self.lcs(s, rs)

        return len(s) - lcs_len


    def lcs(self, s1: str, s2: str) -> int:
        size = len(s1)
        dp = []
        for i in range(size+1):
            dp.append([0] * (size+1))

        for i in range(1, size+1):
            for j in range(1, size+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]

    # recursion + memoization
    # https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/discuss/470684/C%2B%2B-Simple-DP-(Memoization)-and-Bottom-up-with-O(n)-Space

if __name__ == '__main__':
    print(Solution().minInsertions("zzazz"))
    # print(Solution().minInsertions("mbadm"))
    # print(Solution().minInsertions("leetcode"))
    # print(Solution().minInsertions("g"))
    # print(Solution().minInsertions("no"))

    # print(Solution().minInsertions("dyyuyabzkqaybcspq"))
