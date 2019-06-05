#!/usr/bin/env python3

class Solution(object):
    from typing import List
    def _combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) <= 0:
            return []

        candidates.sort()
        res = []

        for i in range(len(candidates)):
            # prune
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates, target, i, [], res)

        print(res)
        return res

    def dfs(self, candidates: List[int], target: int, i: int, curr: List[int], res: List[List[int]]):
        if sum(curr) + candidates[i] > target:
            return
        if sum(curr) + candidates[i] == target:
            curr.append(candidates[i])
            if curr not in res:
                res.append(curr[:])
            curr.pop()
            return
        # continue to search
        curr.append(candidates[i])
        for j in range(i + 1, len(candidates)):
            # need to prune here, or will TLE
            if j > i + 1 and candidates[j] == candidates[j - 1]:
                continue
            if sum(curr) + candidates[j] <= target:
                self.dfs(candidates, target, j, curr, res)
            else:
                break
        curr.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # TODO: another way
        pass

if __name__ == '__main__':
    assert Solution().combinationSum2([10,1,2,7,6,1,5], 8)
    assert Solution().combinationSum2([2,5,2,1,2], 5)