#!/usr/bin/env python3

class Solution(object):
    from typing import List
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        extra = []
        for num in candidates:
            n = target // num
            if n > 1:
                extra.extend([num] * (n-1))
        candidates.extend(extra)

        candidates.sort()
        print(candidates)
        res = []

        for i in range(len(candidates)):
            # prune
            if i > 0 and candidates[i] == candidates[i-1]:
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
        for j in range(i+1, len(candidates)):
            # need to prune here, or will TLE
            if j > i+1 and candidates[j] == candidates[j-1]:
                continue
            if sum(curr) + candidates[j] <= target:
                self.dfs(candidates, target, j, curr, res)
            else:
                break
        curr.pop()

if __name__ == '__main__':
    # assert Solution().combinationSum([2,3,6,7], 7) == [[2,2,3], [7]]
    # assert Solution().combinationSum([2,3,5], 8) == [[2,2,2,2], [2,3,3], [3,5]]
    Solution().combinationSum(
        [92,71,89,74,102,91,70,119,86,116,114,106,80,81,115,99,117,93,76,77,111,110,75,104,95,112,94,73],
        310
    )