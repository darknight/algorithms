#!/usr/bin/env python3

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def _rob(self, nums):
        '''
        Time Limit Exceeded
        '''
        def _f(index):
            if index < 0:
                return 0
            if index == 0:
                return nums[0]
            return max(_f(index-1), nums[index] + _f(index-2))
        return _f(len(nums) - 1)

    def rob(self, nums):
        '''
        f(n) = max(a[n]+f(n-2), f(n-1))
        '''
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        res = [nums[0], max(nums[0], nums[1])]
        i = 2
        while i < len(nums):
            res.append(max(res[i-1], nums[i]+res[i-2]))
            i += 1
        return res[-1]


if __name__ == '__main__':
    print(Solution().rob([1,2,3,4,5,6,7]))
    print(Solution().rob([2,1,1,2]))
    print(Solution().rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]))
