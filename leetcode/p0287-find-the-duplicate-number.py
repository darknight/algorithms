class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Limit Exceeded
        length = len(nums)
        n = length - 1
        sum_val = sum(nums)
        if n == 1:
            return 1
        for target in range(1, n+1):
            min_val = (1+target-1)*(target-1)/2 + (n-target+1)*target + target
            max_val = target*target + (target+1+n)*(n-target)/2 + target
            #print target, min_val, max_val
            if min_val <= sum_val <= max_val:
                k = 0
                for num in nums:
                    if num == target:
                        k += 1
                        if k >= 2:
                            return target

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # refer to https://leetcode.com/discuss/85590/python-solution-with-o-1-space-and-o-nlogn-time
        #TODO: alternative idea http://keithschwarz.com/interesting/code/?dir=find-duplicate
        length = len(nums)
        n = length - 1
        if n == 1:
            return 1
        i = 1
        j = n
        while i < j:
            mid = (i+j)/2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                j = mid
            else:
                i = mid + 1
        return i

if __name__ == '__main__':
    x = range(1, 1000)
    x.append(2)
    print Solution().findDuplicate(x)
