#!/usr/bin/env python3

class Solution(object):
    from typing import List
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                res += 1
                i += 1
            j += 1
        return res

if __name__ == '__main__':
    assert Solution().findContentChildren([1,2,3], [1,1]) == 1
    assert Solution().findContentChildren([1,2], [1,2,3]) == 2