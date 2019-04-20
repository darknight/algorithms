#!/usr/bin/env python3

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []
        res = []
        tmp = [0] * k

        def _combine(i, base, num):
            if i == k:
                if num == 0:
                    res.append(tmp[:])
                return
            for s in range(base, 10):
                tmp[i] = s
                _combine(i+1, s+1, num-s)

        _combine(0, 1, n)
        return res

if __name__ == '__main__':
    print(Solution().combinationSum3(3, 7))
    print(Solution().combinationSum3(3, 9))
    print(Solution().combinationSum3(2, 18))
