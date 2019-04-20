#!/usr/bin/env python3

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #TODO: improve it
        if m == 0:
            return 0
        if m == n:
            return m
        bitm = []
        bitn = []
        while m or n:
            if m:
                bitm.insert(0, m & 0x1)
                m = m >> 1
            if n:
                bitn.insert(0, n & 0x1)
                n = n >> 1
        if len(bitm) != len(bitn):
            return 0
        bitlen = len(bitm)
        res = 0
        for i in range(bitlen):
            if bitm[i] != bitn[i]:
                break
            if bitm[i] == 1:
                res += 1 << (bitlen-i-1)
        return res

if __name__ == '__main__':
    #print(Solution().rangeBitwiseAnd(5, 7))
    print(Solution().rangeBitwiseAnd(4, 5))
