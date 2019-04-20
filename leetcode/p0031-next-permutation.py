#!/usr/bin/env python3

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #TODO: slow, improve
        length = len(nums)
        if length <= 2:
            nums.reverse()
            return
        copy = nums[:]
        copy.sort()
        stop = -1
        for i in range(length-1, 0, -1):
            if nums[i-1] < nums[i]:
                stop = i
                break
        #print(stop)
        if stop < 0:
            nums.sort()
            #print(nums)
            return
        for i in range(stop-1):
            copy.remove(nums[i])
        idx = copy.index(nums[stop-1])
        while copy[idx+1] == copy[idx]:
            idx += 1
        k = idx + 1
        while k > 0:
            copy[k-1], copy[k] =  copy[k], copy[k-1]
            k -= 1
        for i in range(stop-1, length):
            nums[i] = copy[i - (stop-1)]

        #print(nums)

if __name__ == '__main__':
    #Solution().nextPermutation([1,2,3])
    #Solution().nextPermutation([4,6,1,5,3,2])
    #Solution().nextPermutation([3,2,1])
    Solution().nextPermutation([1,5,1])
