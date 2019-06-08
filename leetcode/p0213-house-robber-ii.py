#!/usr/bin/env python3

class Solution(object):
    def rob1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #TODO: slow, improve
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums)
        res = 0
        tmp = [0] * length
        # rob house 0
        tmp[0] = nums[0]
        tmp[1] = nums[0]
        for j in range(2, length-1):
            tmp[j] = max(tmp[j-1], tmp[j-2]+nums[j])
        res = max(res, tmp[-2])
        # not rob house 0
        tmp[0] = 0
        tmp[1] = nums[1]
        for j in range(2, length):
            tmp[j] = max(tmp[j-1], tmp[j-2]+nums[j])
        res = max(res, tmp[-1])
        return res

    from typing import List
    def rob(self, nums: List[int]) -> int:
        """
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        (1) i [0, n-1]
        (2) i [1, n]
        """
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        # WA a few times for dp1, dp1[1] must be equal to dp1[0]
        dp1 = [nums[0], nums[0]]  # must steal first house
        dp2 = [0, nums[1]]  # must not steal first house
        for i in range(2, len(nums) - 1):
            val = max(dp1[i-1], dp1[i-2]+nums[i])
            dp1.append(val)
        for i in range(2, len(nums)):
            val = max(dp2[i-1], dp2[i-2]+nums[i])
            dp2.append(val)
        return max(dp1[-1], dp2[-1])


if __name__ == '__main__':
    assert Solution().rob([4,1,2,7,5,3,1]) == 14
    assert Solution().rob([1,3,1,3,100]) == 103
    assert Solution().rob([2,3,2]) == 3
    assert Solution().rob([1,2,3,1]) == 4
    assert Solution().rob([1,1,1]) == 1
    assert Solution().rob([1,2,3,4,5,6,7,8,7,6,5,4,3,2,1]) == 32
