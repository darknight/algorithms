class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        '''
        f[i] = max(f[i-1] + xi, xi)
        '''
        if len(A) == 0:
            return 0
        max_sum = A[0]
        curr_sum = 0
        for x in A:
            if curr_sum > 0:
                curr_sum = curr_sum + x
            else:
                curr_sum = x
            max_sum = max(max_sum, curr_sum)
        return max_sum

    # TODO: divide & conquer
    def maxSubArray2(self, A):
        pass

if __name__ == '__main__':
    print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print Solution().maxSubArray([1,-2,3,10,-4,7,2,-5])
    print Solution().maxSubArray([-5])

