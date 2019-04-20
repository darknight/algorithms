class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #TODO: slow & improve
        length = len(nums)
        if length == 0:
            return [[]]
        if length == 1:
            return [nums]
        nums.sort()
        res = []

        def _permute(start, stop):
            if start == stop:
                res.append(nums[:])
                return
            head = set()
            for i in range(start, stop+1):
                if nums[i] in head:
                    continue
                head.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]
                _permute(start+1, stop)
                nums[start], nums[i] = nums[i], nums[start]

        _permute(0, length-1)
        return res

if __name__ == '__main__':
    #print Solution().permuteUnique([1,2,3])
    #print Solution().permuteUnique([1,2,3,4])
    print Solution().permuteUnique([1,1,2])
    print Solution().permuteUnique([1,2,2])
    print Solution().permuteUnique([1,1,1,2])
    print Solution().permuteUnique([1,1,2,2])
