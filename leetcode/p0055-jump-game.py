#!/usr/bin/env python3

from typing import List

class Solution(object):
    def AC_canJump(self, nums):
        """
        slow solution
        """
        length = len(nums)
        if length == 0:
            return False
        if length == 1:
            return True
        tmp = [0] * length
        tmp[0] = nums[0]
        for i in range(1, length):
            if tmp[i-1] < i:
                tmp[i] = 0
            elif tmp[i-1] == i:
                tmp[i] = nums[i] + i
            else:
                tmp[i] = max(tmp[i-1], nums[i]+i)
        return tmp[-1] > 0

    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        if size == 0:
            return False
        if size == 1:
            return True
        furthest = nums[0]
        for i in range(1, size):
            if furthest < i:
                return False
            furthest = max(furthest, i + nums[i])

        return furthest >= size - 1


if __name__ == '__main__':
    print(Solution().canJump([2,3,1,1,4]))
    print(Solution().canJump([3,2,1,0,4]))
