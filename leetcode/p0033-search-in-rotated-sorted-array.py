#!/usr/bin/env python3

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        
        if len(nums) < 1:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        index = -1
        if nums[-1] == target:
            index = len(nums) - 1
        elif nums[-1] < target:
            i = 0
            while i < len(nums):
                if nums[i] == target:
                    index = i
                    break
                else:
                    i += 1
        else:
            i = len(nums) - 1
            while i >= 0:
                if nums[i] == target:
                    index = i
                    break
                else:
                    i -= 1
        return index


if __name__ == '__main__':
    print(Solution().search([4,5,6,0,1,2,3], 2))
    print(Solution().search([4,5,6,0,1,2,3], 6))
    print(Solution().search([1], 0))
