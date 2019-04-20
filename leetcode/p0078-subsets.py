#!/usr/bin/env python3

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length == 0:
            return [[]]
        res = []
        nums.sort()
        mask = [1<<i for i in range(length-1, -1, -1)]
        for i in range(2 ** length):
            tmp = []
            for j, m in enumerate(mask):
                if m & i:
                    tmp.append(nums[j])
            res.append(tmp)
        return res

if __name__ == '__main__':
    print(Solution().subsets([]))
    print(Solution().subsets([1]))
    print(Solution().subsets([1,2]))
    print(Solution().subsets([3,2,1]))
    print(Solution().subsets([1,3,2,4]))
