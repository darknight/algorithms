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

    def TLE_dfs(self, chars, tmp, res: List[int]):

        for ch in chars:
            if ch.isdisjoint(tmp):
                tmp = tmp.union(ch)
                res[0] = max(res[0], len(tmp))
                self.dfs(chars, tmp, res)
                tmp = tmp.difference(ch)
            else:
                continue

    def dfs(self, chars, idx, tmp, res):
        res[0] = max(res[0], len(tmp))
        for i in range(idx, len(chars)):
            ch = chars[i]
            if ch.isdisjoint(tmp):
                self.dfs(chars, i, tmp.union(ch), res)

    def maxLength(self, arr: List[str]) -> int:
        """
        based on the discussion: could solve it by DFS + backtracking
        """
        if len(arr) == 1:
            return len(arr[0])

        chars = []
        for item in arr:
            if len(item) == len(set(item)):
                chars.append(set(item))

        res = [0]
        self.dfs(chars, 0, set(), res)

        print(res)
        return res[0]

    # TODO: use DP

if __name__ == '__main__':
    assert Solution().maxLength(["un", "iq", "ue"]) == 4
    assert Solution().maxLength(["cha", "r", "act", "ers"]) == 6
    assert Solution().maxLength(
        ["cusy", "s", "imelfbpuoawkrq", "roxckjm", "vkaxcbespwotzq", "jrnhyslwbifteqox", "fnisjhckr", "ubvpwtzxh",
         "sgxkqdlw", "hzsngeotfxbcm", "zhrextvndpcmbql", "bdfxez", "rzgnbf", "hbw", "cohurlnjqpefzayig",
         "xoqgyjsm"]) == 18
    assert Solution().maxLength(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]) == 16
