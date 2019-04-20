#!/usr/bin/env python3

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        length = len(nums)
        real_sum = (1 + length) * length / 2
        res = real_sum - total
        return res

if __name__ == '__main__':
    print(Solution().missingNumber([0,1,3]))
