#!/usr/bin/env python3

class Solution(object):
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        vowels = ('a', 'e', 'i', 'o', 'u')
        ss = list(s)
        while i < j:
            if ss[i].lower() not in vowels:
                i += 1
            elif ss[j].lower() not in vowels:
                j -= 1
            else:
                ss[i], ss[j] = ss[j], ss[i]
                i += 1
                j -= 1

        return "".join(ss)

if __name__ == '__main__':
    assert Solution().reverseVowels("hello") == "holle"
    assert Solution().reverseVowels("leetcode") == "leotcede"