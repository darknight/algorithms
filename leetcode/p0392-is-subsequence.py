#!/usr/bin/env python3

class Solution(object):
    from typing import List
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        i = 0
        for ch in t:
            if s[i] == ch:
                i += 1
                if i == len(s):
                    break
        return i == len(s)



if __name__ == '__main__':
    assert Solution().isSubsequence("abc", "ahbgdc") == True
    assert Solution().isSubsequence("axc", "ahbgdc") == False