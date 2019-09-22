#!/usr/bin/env python3

from typing import List
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        if len(mat) == 1:
            return -1
        base = set([i for i in range(1, 10**4 + 1)])
        for row in mat:
            s = set(row)
            base = base & s

        res = list(base)
        res.sort()
        if len(res) == 0:
            return -1
        return res[0]

if __name__ == '__main__':
    assert Solution().smallestCommonElement([[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]) == 5