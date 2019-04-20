#!/usr/bin/env python3

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        n = 0
        for i in range(size):
            if nums[i] == 0:
                n += 1
            else:
                nums[i-n] = nums[i]
        for i in range(size-n, size):
            nums[i] = 0

if __name__ == '__main__':
    Solution().moveZeroes([0,1,0,3,12])
    Solution().moveZeroes([0,0,1])

