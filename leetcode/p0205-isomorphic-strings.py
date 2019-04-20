#!/usr/bin/env python3

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if len(s) <= 1:
            return True
        charmap = {}
        charlist = []
        for i, c in enumerate(s):
            if c not in charmap:
                charmap[c] = t[i]
                if t[i] not in charlist:
                    charlist.append(t[i])
                else:
                    return False
            elif charmap[c] != t[i]:
                return False
        return True

if __name__ == '__main__':
    print(Solution().isIsomorphic('title', 'paper'))
    print(Solution().isIsomorphic('egg', 'add'))
    print(Solution().isIsomorphic('foo', 'bar'))
    print(Solution().isIsomorphic('bar', 'foo'))
