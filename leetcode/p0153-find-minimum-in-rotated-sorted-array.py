#!/usr/bin/env python3

class Solution:
    # @param num, a list of integer
    # @return an integer
    def _findMin(self, num):
        '''
        passed
        '''
        return min(num)

    def _findMin(self, num):
        '''
        passed
        '''
        if len(num) == 0:
            return
        ret = num[0]
        for x in num:
            if x < ret:
                ret = x
                break
        return ret

    from typing import List
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        h = len(nums) - 1
        while l < h:
            m = l + (h - l) // 2
            if nums[m] > nums[h]: # min is in [m+1, h]
                l = m + 1
            else:
                h = m
        return nums[l]


if __name__ == '__main__':
    print(Solution().findMin([4,5,6,7,0,1,2]))
