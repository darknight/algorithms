class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        i = 0
        j = len(A) - 1
        idx = -1
        while i <= j:
            mid = (i + j) / 2
            if target > A[mid]:
                i = i + 1
            elif target < A[mid]:
                j = j - 1
            else:
                idx = mid
                break
        if idx == -1:
            idx = i
        return idx

if __name__ == '__main__':
    print Solution().searchInsert([1,3,5,6], 5)
    print Solution().searchInsert([1,3,5,6], 2)
    print Solution().searchInsert([1,3,5,6], 7)
    print Solution().searchInsert([1,3,5,6], 0)
