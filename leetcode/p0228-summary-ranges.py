class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        start = nums[0]
        prev = start
        i = 1
        res = []
        nums.append(start) # sentinel element
        length = len(nums)
        while i < length:
            curr = nums[i]
            if curr - prev == 1:
                prev = curr
            else:
                if start == prev:
                    res.append('%s' % start)
                else:
                    res.append('%s->%s' % (start, prev))
                start = curr
                prev = curr
            i += 1
        return res

if __name__ == '__main__':
    print Solution().summaryRanges([0,1,2,4,5,7])
    print Solution().summaryRanges([0,1,2,3,4,5])
