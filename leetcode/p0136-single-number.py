class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        res = 0
        for i in A:
            res = res ^ i
        return res

print Solution().singleNumber([1,2,3,4,5,4,3,2,1])
