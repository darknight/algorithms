#!/usr/bin/env python3

from typing import List

class Solution(object):
    def _productExceptSelf(self, nums):
        """
        Time Limit Exceeded
        """
        length = len(nums)
        res = [1] * length
        for i in range(length-1):
            h = nums.pop(0)
            nums.append(h)
            for j, v in enumerate(nums):
                res[j] = res[j] * v

        return res

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        if length < 2:
            return nums
        # sentinel
        nums.insert(0, 1)
        nums.append(1)
        prefix = nums[:]
        suffix = nums[:]
        res = [1] * length
        for i in range(1, length):
            prefix[i] = prefix[i] * prefix[i-1]
        for i in range(length, 1, -1):
            suffix[i] = suffix[i] * suffix[i+1]
        for i in range(1, length+1):
            res[i-1] = prefix[i-1] * suffix[i+1]

        return res

    def AC_productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        res[i] = prefix[i-1] + suffix[i+1]
        """
        size = len(nums)
        if size <= 1:
            return nums
        res = [1] * size
        for i in range(1, size):
            res[i] = res[i - 1] * nums[i - 1]
        suffix = 1
        for j in range(size - 1, -1, -1):
            res[j] = res[j] * suffix
            suffix = suffix * nums[j]

        return res

if __name__ == '__main__':
    print(Solution().productExceptSelf([1,2,3,4]))
    print(Solution().productExceptSelf([1,2]))
