#!/usr/bin/env python3

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # refer to https://soulmachine.gitbooks.io/algorithm-essentials/content/java/linear-list/array/3sum.html
        #TODO: improve
        nums.sort()
        length = len(nums)
        if length < 3:
            return []
        if length == 3:
            if sum(nums) == 0:
                return [nums]
            return []
        tmp = set()
        for i in range(length-2):
            a = nums[i]
            if a > 0:
                break
            j = i+1
            k = length-1
            while j < k:
                b = nums[j]
                c = nums[k]
                if a + b + c == 0:
                    tmp.add((a, b, c))
                    k -= 1
                    j += 1
                elif a + b + c > 0:
                    k -= 1
                else:
                    j += 1
        res = []
        for s in tmp:
            res.append(list(s))
        return res

if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSum([-2, 0, 1, 1, 2]))
