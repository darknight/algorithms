#!/usr/bin/env python3

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        m = {}
        base = ord('a')
        for c in range(base, ord('z')+1):
            m[chr(c)] = 1 << (c-base)

        ints = []
        for word in words:
            num = 0
            for c in word:
                num = num | m[c]
            ints.append(num)

        res = 0
        for i in range(len(ints)-1):
            for j in range(i+1, len(ints)):
                if ints[i] & ints[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        
        return res

if __name__ == '__main__':
    print(Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
    print(Solution().maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
    print(Solution().maxProduct(["a", "aa", "aaa", "aaaa"]))
