#!/usr/bin/env python3

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return []
        res = []
        tmp = [0] * k
        def _func(i, start, k2):
            if i == k:
                res.append(tmp[:])
                return
            stop = n - k2 + 1
            for x in range(start, stop+1):
                tmp[i] = x
                _func(i+1, x+1, k2-1)

        _func(0, 1, k)
        return res

if __name__ == '__main__':
    print(Solution().combine(4, 1))
    print(Solution().combine(4, 2))
    print(Solution().combine(4, 3))
    print(Solution().combine(4, 4))
