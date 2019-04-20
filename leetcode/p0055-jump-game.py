class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #TODO: slow & improve
        length = len(nums)
        if length == 0:
            return False
        if length == 1:
            return True
        tmp = [0] * length
        tmp[0] = nums[0]
        for i in range(1, length):
            if tmp[i-1] < i:
                tmp[i] = 0
            elif tmp[i-1] == i:
                tmp[i] = nums[i] + i
            else:
                tmp[i] = max(tmp[i-1], nums[i]+i)
        return tmp[-1] > 0

if __name__ == '__main__':
    print Solution().canJump([2,3,1,1,4])
    print Solution().canJump([3,2,1,0,4])
