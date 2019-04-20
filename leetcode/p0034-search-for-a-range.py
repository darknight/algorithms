#!/usr/bin/env python3

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
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
            mid = (i + j) / 2
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
            mid = (i + j) / 2
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

if __name__ == '__main__':
    print(Solution().searchRange([1,2,3,4,5,7,7,8,9,10], 8))

