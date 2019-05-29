#!/usr/bin/env python3

class Solution(object):
    from typing import List
    # TODO: slow, improve
    def findCircleNum(self, M: List[List[int]]) -> int:
        res = 0
        for i in range(len(M)):
            if self.has_friend(i, M):
                res += 1

        return res

    def has_friend(self, i, M: List[List[int]]) -> bool:
        res = False
        for j in range(len(M[i])):
            if M[i][j] == 1:
                M[i][j] = 2
                M[j][i] = 2
                self.has_friend(j, M)
                res = True
        return res


if __name__ == '__main__':
    assert Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2
    assert Solution().findCircleNum([[1,1,0],[1,1,1],[0,1,1]]) == 1