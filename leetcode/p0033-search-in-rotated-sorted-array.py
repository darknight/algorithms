#!/usr/bin/env python3

from typing import List

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def AC_search(self, nums, target):
        
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

    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size == 0:
            return -1
        if size <= 1:
            if nums[0] == target:
                return 0
            return -1

        low = nums[0]
        high = nums[-1]
        if target == low:
            return 0
        if target == high:
            return size - 1
        if high < target < low:
            return -1

        i = 0
        j = size - 1
        while i <= j:
            k = i + (j - i) // 2
            if target == nums[k]:
                return k
            if target > low:
                if nums[k] < low:
                    j = k - 1
                elif target < nums[k]:
                    j = k - 1
                else:
                    i = k + 1
            if target < high:
                if nums[k] > high:
                    i = k + 1
                elif target < nums[k]:
                    j = k - 1
                else:
                    i = k + 1

        return -1


if __name__ == '__main__':
    # print(Solution().search([4,5,6,0,1,2,3], 2))
    # print(Solution().search([4,5,6,0,1,2,3], 6))
    # print(Solution().search([1], 0))
    assert Solution().search([], 5) == -1
    assert Solution().search(nums = [4,5,6,7,0,1,2], target = 3) == -1
    assert Solution().search(nums = [4,5,6,7,0,1,2], target = 4) == 0
    assert Solution().search(nums = [4,5,6,7,0,1,2], target = 7) == 3
    assert Solution().search(nums = [4,5,6,7,0,1,2], target = 0) == 4
    assert Solution().search(nums = [4,5,6,7,0,1,2], target = 1) == 5
    assert Solution().search(nums = [4,5,6,7,0,1,2], target = 2) == 6

    assert Solution().search(nums = [0,1,2,4,5,6,7], target = 0) == 0
    assert Solution().search(nums = [0,1,2,4,5,6,7], target = 1) == 1
    assert Solution().search(nums = [0,1,2,4,5,6,7], target = 3) == -1
    assert Solution().search(nums = [0,1,2,4,5,6,7], target = 6) == 5
    assert Solution().search(nums = [0,1,2,4,5,6,7], target = 7) == 6
