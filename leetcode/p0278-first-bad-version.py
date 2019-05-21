#!/usr/bin/env python3

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return False

class Solution:

    # assume there always exists a bad version
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        l = 1
        h = n
        while l < h:
            m = l + (h - l) // 2
            if isBadVersion(m):
                h = m
            else:
                l = m + 1

        return l


if __name__ == '__main__':
    pass