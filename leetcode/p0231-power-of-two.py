#!/usr/bin/env python3

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n > 1:
            if n & 0x1 == 1:
                return False
            n = n >> 0x1
        return True

if __name__ == '__main__':
    print(Solution().isPowerOfTwo(63))
    print(Solution().isPowerOfTwo(64))
