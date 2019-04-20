class Solution(object):
    def _productExceptSelf(self, nums):
        """
        Time Limit Exceeded
        """
        length = len(nums)
        res = [1] * length
        for i in range(length-1):
            h = nums.pop(0)
            nums.append(h)
            for j, v in enumerate(nums):
                res[j] = res[j] * v

        return res

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        if length < 2:
            return nums
        # sentinel
        nums.insert(0, 1)
        nums.append(1)
        prefix = nums[:]
        suffix = nums[:]
        res = [1] * length
        for i in range(1, length):
            prefix[i] = prefix[i] * prefix[i-1]
        for i in range(length, 1, -1):
            suffix[i] = suffix[i] * suffix[i+1]
        for i in range(1, length+1):
            res[i-1] = prefix[i-1] * suffix[i+1]

        return res

if __name__ == '__main__':
    print Solution().productExceptSelf([1,2,3,4])
    print Solution().productExceptSelf([1,2])
