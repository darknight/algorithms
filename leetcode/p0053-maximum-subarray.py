#!/usr/bin/env python3

from typing import List

class Solution:
    # @param A, a list of integers
    # @return an integer
    def DP_maxSubArray(self, nums: List[int]):
        '''
        f(i) = (f(i-1) > 0 ? f(i-1) : 0) + A[i]
        '''
        size = len(nums)
        if size == 0:
            return 0
        dp = [0] * size
        dp[0] = nums[0]
        for i in range(1, size):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)

    # TODO: divide & conquer
    def maxSubArray(self, nums: List[int]):
        pass

if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(Solution().maxSubArray([1,-2,3,10,-4,7,2,-5]))
    print(Solution().maxSubArray([-5]))

