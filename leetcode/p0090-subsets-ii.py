#!/usr/bin/env python3

class Solution(object):
    from typing import List
    def subsetsWithDup1(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [[], nums]

        nums.sort()
        res = [[]]

        for size in range(1, len(nums) + 1):
            for i in range(len(nums) - size + 1):
                self.dfs(size, i, [], nums, res)

        print(res)
        return res

    def dfs(self, size: int, i: int, curr: List[int], nums: List[int], res: List[List[int]]):
        curr.append(nums[i])
        if len(curr) == size:
            if curr not in res:
                res.append(curr[:])
            curr.pop()
            return
        for j in range(i+1, len(nums)):
            self.dfs(size, j, curr, nums, res)
        curr.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #TODO: another method
        pass

if __name__ == '__main__':
    Solution().subsetsWithDup([1,2,2])
    Solution().subsetsWithDup([1,1,2,2])
    Solution().subsetsWithDup([1,2,2,3])