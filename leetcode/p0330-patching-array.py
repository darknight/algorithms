#!/usr/bin/env python3

class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        #TODO: slow & improve
        nums.sort()
        if n < 1:
            return 0
        length = len(nums)
        if length == 0 or (length > 0 and nums[0] != 1):
            patch = 1
            start = 0
        else:
            patch = 0
            start = 1
        longest = 1
        #print('patch', patch)
        #print('longest', longest)
        while start < length:
            if longest >= n:
                break
            if longest >= nums[start] or longest == nums[start] - 1:
                longest += nums[start]
                start += 1
            else:
                patch += 1
                longest += longest + 1
        #print('patch', patch)
        #print('longest', longest)
        while longest < n:
            patch += 1
            longest += longest + 1
        return patch

if __name__ == '__main__':
    #print(Solution().minPatches([1,3], 6))
    #print(Solution().minPatches([1,5,10], 20))
    #print(Solution().minPatches([1,2,2], 5))
    print(Solution().minPatches([], 31))
