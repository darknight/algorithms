#!/usr/bin/env python3

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if len(nums) <= 1:
            return False
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] ^ nums[i+1] == 0:
                return True
        return False

if __name__ == '__main__':
    print(Solution().containsDuplicate([5,6,7,2,3,4,8]))
    print(Solution().containsDuplicate([5,5]))
