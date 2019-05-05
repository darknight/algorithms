#!/usr/bin/env python3

from typing import List

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def _findKthLargest(self, nums, k):
        if len(nums) == 1:
            return nums[0]
        nums.sort(reverse=True)
        return nums[k-1]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        self._partition(nums, 0, len(nums) - 1, target)
        return nums[target]

    def _partition(self, nums: List[int], start, end, target):
        if start >= end:
            return
        i = start
        j = end
        pivot = nums[j]
        while i < j:
            while i < j and nums[i] < pivot:
                i += 1
            while i < j and nums[j] >= pivot:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[end] = nums[i]
        nums[i] = pivot
        if i <= target:
            self._partition(nums, i+1, end, target)
        else:
            self._partition(nums, start, j-1, target)

if __name__ == '__main__':
    assert Solution().findKthLargest([3,2,1,5,6,4,6], 2) == 6
    assert Solution().findKthLargest([-1,-1], 2) == -1
    assert Solution().findKthLargest([3,2,1,5,6,4], 2) == 5
    assert Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
