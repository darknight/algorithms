#!/usr/bin/env python3

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums2 = sorted(nums)
        i = 0
        j = len(nums2) - 1
        while i < j:
            a = nums2[i]
            b = nums2[j]
            if a + b > target:
                j -= 1
            elif a + b < target:
                i += 1
            else:
                break
        a = nums2[i]
        b = nums2[j]
        i = nums.index(a)
        if a == b:
            j = nums.index(a, i+1)
        else:
            j = nums.index(b)
        return [i, j]

if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum([0, 4, 3, 0], 0))