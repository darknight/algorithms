#!/usr/bin/env python3

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def _strStr(self, haystack, needle):
        return haystack.find(needle)

    def strStr(self, haystack, needle):
        if len(needle) > len(haystack):
            return -1
        if needle == "":
            return 0
        step = len(needle)
        for i in range(len(haystack) - step + 1):
            temp_str = haystack[i:i+step]
            if temp_str == needle:
                return i
        return -1

if __name__ == '__main__':
    print(Solution().strStr("", ""))
    print(Solution().strStr("a", "a"))

