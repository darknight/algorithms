#!/usr/bin/env python3

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def _searchRange(self, nums, target):
        error = [-1, -1]
        length = len(nums)
        if length == 0:
            return error
        if length == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return error
        i = 0
        j = length - 1
        lower = -1
        upper = -1
        while i <= j and i < length and j >= 0:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                if nums[i] < target:
                    i += 1
                else:
                    lower = i
                    break

        i = 0
        j = length - 1
        while i <= j and i < length and j >= 0:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                if nums[j] > target:
                    j -= 1
                else:
                    upper = j
                    break
        if lower == -1 or upper == -1:
            return error
        return [lower, upper]

    from typing import List
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        from typing import List
        def binary_search(nums: List[int], target: int) -> int:
            l = 0
            h = len(nums)  # from 3rd party
            while l < h:
                m = l + (h - l) // 2
                if nums[m] >= target:
                    h = m
                else:
                    l = m + 1
            return l

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1,-1]
        low = binary_search(nums, target)
        if low >= len(nums) or nums[low] != target:
            return [-1, -1]
        high = binary_search(nums, target+1)
        return [low, high-1]


if __name__ == '__main__':
    assert Solution().searchRange([1,2,3,4,5,7,7,8,9,10], 8) == [7,7]
    assert Solution().searchRange([5,7,7,8,8,10], 8) == [3,4]
    assert Solution().searchRange([5,7,7,8,8,10], 6) == [-1,-1]
    assert Solution().searchRange([2,2], 2) == [0,1]

