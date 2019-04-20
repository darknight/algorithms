#!/usr/bin/env python3

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        weight = 0
        while n != 0:
            weight += n & 0x1
            n = n >> 1
        return weight

if __name__ == '__main__':
    print(Solution().hammingWeight(11))
