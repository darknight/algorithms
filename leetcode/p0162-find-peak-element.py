#!/usr/bin/env python3

from typing import List

class Solution:
    # @param num, a list of integer
    # @return an integer
    def WA_findPeakElement(self, num):
        length = len(num)
        if length == 0:
            return -1
        if length == 1:
            return 0
        num.insert(0, float('-inf'))
        num.append(float('-inf'))
        res = [-1]

        def peakElement(start, stop):
            if res[0] != -1:
                return
            if start > stop:
                return
            mid = (start + stop) / 2
            if num[mid] > num[mid-1] and num[mid] > num[mid+1]:
                res[0] = mid
                return
            # here it's not O(logN)
            peakElement(start, mid-1)
            peakElement(mid+1, stop)

        peakElement(1, length)
        return res[0] - 1

    def AC_findPeakElement(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return 0
        res = [-1]
        self.bin_search(0, size - 1, size, nums, res)
        return res[0]

    def bin_search(self, i: int, j: int, size: int, nums: List[int], res: List[int]):
        if res[0] > -1:
            return
        while i <= j:
            mid = i + (j - i) // 2
            if mid == 0:
                if nums[0] > nums[1]:
                    res[0] = 0
                    return
                else:
                    i = mid + 1
            elif mid == size - 1:
                if nums[mid] > nums[mid - 1]:
                    res[0] = mid
                    return
                else:
                    j = mid - 1
            else:
                if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                    res[0] = mid
                    return
                elif nums[mid] < nums[mid + 1]:
                    i = mid + 1
                else:
                    j = mid - 1

    # TODO
    def findPeakElement(self, nums: List[int]) -> int:
        """
        much shorter solution:
        https://leetcode.com/problems/find-peak-element/discuss/50232/Find-the-maximum-by-binary-search-(recursion-and-iteration)
        """
        pass

if __name__ == '__main__':
    assert Solution().findPeakElement([1]) == 0
    assert Solution().findPeakElement([1,2]) == 1
    assert Solution().findPeakElement([1,2,3]) == 2
    assert Solution().findPeakElement([1,3,1]) == 1
    assert Solution().findPeakElement([1,2,3,4,5,1,2,3,4]) == 4
