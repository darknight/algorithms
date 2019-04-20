#!/usr/bin/env python3

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        words = s.split()
        if len(words) == 0:
            return 0
        return len(words[-1])

    # TODO: not use built-in function
    def lengthOfLastWord2(self, s):
        pass

if __name__ == '__main__':
    print(Solution().lengthOfLastWord("Hello World"))
    print(Solution().lengthOfLastWord("Hello"))
    print(Solution().lengthOfLastWord("Hello "))
    print(Solution().lengthOfLastWord(""))
    print(Solution().lengthOfLastWord("  "))
