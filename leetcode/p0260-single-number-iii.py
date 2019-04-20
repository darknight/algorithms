class Solution(object):
    '''
    refer to
    https://leetcode.com/discuss/84962/concise-c-solution-bit-manipulation
    '''

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a_xor_b = 0
        for i in nums:
            a_xor_b = a_xor_b ^ i

        mask = a_xor_b & (~a_xor_b + 1)
        a = b = 0
        for i in nums:
            if i & mask:
                a = a ^ i
            else:
                b = b ^ i

        return [a, b]

if __name__ == '__main__':
    print Solution().singleNumber([1,2,3,2,1,5,4,4,6,6])
