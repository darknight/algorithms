class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #TODO: slow, improve
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums)
        res = 0
        tmp = [0] * length
        # rob house 0
        tmp[0] = nums[0]
        tmp[1] = nums[0]
        for j in range(2, length-1):
            tmp[j] = max(tmp[j-1], tmp[j-2]+nums[j])
        res = max(res, tmp[-2])
        # not rob house 0
        tmp[0] = 0
        tmp[1] = nums[1]
        for j in range(2, length):
            tmp[j] = max(tmp[j-1], tmp[j-2]+nums[j])
        res = max(res, tmp[-1])
        return res

if __name__ == '__main__':
    print Solution().rob([1,1,1])
    print Solution().rob([1,2,3,4,5,6,7,8,7,6,5,4,3,2,1])
