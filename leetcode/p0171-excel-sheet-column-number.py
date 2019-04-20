#!/usr/bin/env python3

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        D = {}
        start = ord('A')
        for i in range(0, 26):
            D[chr(start + i)] = i + 1
        num = 0
        for i, c in enumerate(reversed(s)):
            num += D[c] * (26 ** i)
        return num

print(Solution().titleToNumber('B'))
print(Solution().titleToNumber('Z'))
print(Solution().titleToNumber('AA'))
print(Solution().titleToNumber('AB'))
