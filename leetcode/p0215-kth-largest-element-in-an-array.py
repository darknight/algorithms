#!/usr/bin/env python3

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        if len(nums) == 1:
            return nums[0]
        nums.sort(reverse=True)
        return nums[k-1]


if __name__ == '__main__':
    print(Solution().findKthLargest([3,2,1,5,6,4,6], 2))
    print(Solution().findKthLargest([-1,-1], 2))
