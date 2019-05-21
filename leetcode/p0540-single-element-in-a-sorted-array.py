#!/usr/bin/env python3

class Solution(object):
    from typing import List

    # O(n)
    def _singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]

        return res

    # O(log n)
    def singleNonDuplicate1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        h = len(nums) - 1
        while l < h:
            m = l + (h - l) // 2
            if (m - l) % 2 == 0:
                if nums[m] == nums[m-1]:
                    h = m
                else:
                    l = m
            else:
                if nums[m] == nums[m-1]:
                    l = m + 1
                elif nums[m] == nums[m+1]:
                    h = m - 1
                else:
                    return nums[m]
        return nums[l]

    # TODO
    def singleNonDuplicate1(self, nums: List[int]) -> int:
        pass


if __name__ == '__main__':
    assert Solution().singleNonDuplicate([1, 1, 2]) == 2
    assert Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8]) == 2
    assert Solution().singleNonDuplicate([3,3,7,7,10,11,11]) == 10