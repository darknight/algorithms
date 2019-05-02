#!/usr/bin/env python3

class Solution(object):
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                break
        return self._is_palindrome(s[i+1:j+1]) or self._is_palindrome(s[i:j])

    def _is_palindrome(self, s) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

if __name__ == '__main__':
    assert Solution().validPalindrome("aba") is True
    assert Solution().validPalindrome("abca") is True