#!/usr/bin/env python3

from typing import List
from collections import defaultdict

class Solution(object):
    # TODO: too slow, improve
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res = ""
        s_set = set(s)
        for word in d:
            if s_set.issuperset(set(word)) and self._is_substring(s, word):
                if len(word) > len(res):
                    res = word
                elif len(word) == len(res) and word < res:
                    res = word
                else:
                    pass
        return res

    def _is_substring(self, s, word) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                j += 1
            i += 1
        return j == len(word)


if __name__ == '__main__':
    assert Solution().findLongestWord("abpcplea", ["ale","apple","monkey","plea"]) == "apple"
    assert Solution().findLongestWord("abpcplea", ["a","b","c"]) == "a"
    assert Solution().findLongestWord("bab", ["ba", "ab", "a", "b"]) == "ab"