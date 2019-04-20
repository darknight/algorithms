#!/usr/bin/env python3

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        if len(nums) == 0:
            return
        for i in range(k):
            x = nums.pop()
            nums.insert(0, x)

    # TODO
    def rotate2(self, nums, k):
        pass

    # TODO
    def rotate3(self, nums, k):
        pass

if __name__ == '__main__':
    x = [1,2]
    Solution().rotate(x, 1)
    print(x)
