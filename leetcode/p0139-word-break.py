#!/usr/bin/env python3

import math
import itertools
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass

try:
    from _list import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass


class Solution:
    def TLE_1_WA_wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [False]
        self.chop([s], wordDict, res)

        return res[0]

    def chop(self, ss: List[str], words: List[str], res: List[bool]):
        if res[0] is True:
            return
        if len(ss) == 0:
            res[0] = True
            return
        for i in range(len(words)):
            w = words[i]
            tmp = []
            for s in ss:
                idx = s.find(w)
                while idx != -1:
                    left = s[:idx]
                    right = s[idx+len(w):]
                    if left != "":
                        tmp.append(left)
                    s = right
                    idx = s.find(w)
                if s != "":
                    tmp.append(s)
            self.chop(tmp, words[:i] + words[i+1:], res)


    def TLE_2_wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        res = [False]
        self.TLE_2_dfs(s, words, res)

        return res[0]

    def TLE_2_dfs(self, s: str, words: Set[str], res: List[bool]):
        if res[0] is True:
            return
        if s == "":
            res[0] = True
            return
        for end in range(1, len(s) + 1):
            prefix = s[:end]
            if prefix in words: # prefix could be same in multiple call of `dfs`
                self.TLE_2_dfs(s[end:], words, res)


    def WA_wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        f(i,j) = f(i-len(wj)) && a[i-len(wj):i] == wj
        """
        wsize = len(wordDict)
        chsize = len(s)

        dp = []
        for _ in range(chsize+1):
            dp.append([False] * (wsize+1))

        for j in range(wsize+1):
            dp[0][j] = True

        for i in range(1, chsize+1):
            for j in range(1, wsize+1):
                w = wordDict[j-1]
                if i < len(w):
                    continue
                if dp[i-len(w)][j] is True and s[i-len(w):i] == w:
                    dp[i][j] = True

        return any(dp[-1])


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        f(i) = f(i-len(w) && a[i-len(w):i] for all w in wordDict
        this is almost the same as WA version
        """
        chsize = len(s)
        dp = [False] * (chsize + 1)
        dp[0] = True

        for i in range(1, chsize+1):
            for w in wordDict:
                if i < len(w):
                    continue
                if dp[i-len(w)] and s[i-len(w):i] == w:
                    dp[i] = True

        return dp[-1]


    # TODO: BFS
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:

if __name__ == '__main__':
    assert Solution().WA_wordBreak(s = "leetcode", wordDict = ["leet", "code"]) is True
    assert Solution().WA_wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]) is True
    assert Solution().WA_wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]) is False
    assert Solution().WA_wordBreak("cbca", ["bc","ca"]) is False
    assert Solution().WA_wordBreak(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    ) is False
