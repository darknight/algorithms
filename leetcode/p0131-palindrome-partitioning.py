#!/usr/bin/env python3

class Solution(object):
    from typing import List
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return []
        if len(s) == 1:
            return [[s]]

        res = []
        for i in range(len(s)):
            if i > 0 and s[i] != s[0]:
                continue
            self.dfs(i+1, s[0:i+1], [], s, res)

        print(res)
        return res

    def dfs(self, next: int, prefix: str, curr: List[str], s: str, res: List[List[str]]):
        if self.is_palindrome(prefix) is False:
            return

        curr.append(prefix)
        if next >= len(s):
            res.append(curr[:])
            curr.pop()
            return

        for j in range(next, len(s)):
            if j > next and s[j] != s[next]:
                continue
            self.dfs(j + 1, s[next:j+1], curr, s, res)
        curr.pop()

    def is_palindrome(self, s: str):
        if len(s) <= 1:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    Solution().partition("aab")
    Solution().partition("aabb")