class Solution:
    # @param a list of integers
    # @return an integer

    def removeDuplicates(self, A):
        length = len(A)
        if length < 3:
            return length
        i = 1
        curr = A[0]
        while i < length - 1:
            if A[i] == curr:
                if A[i+1] == curr:
                    A[i] = float('inf')
                    i += 1
                else:
                    curr = A[i+1]
                    i += 2
            else:
                curr = A[i]
                i += 1
        i = 0
        j = i + 1
        while i < length-1 and j < length:
            while j < length and A[j] == float('inf'):
                j += 1
            while j < length and A[j] != float('inf'):
                A[i+1] = A[j]
                i += 1
                j += 1
        A = A[:i+1]
        return len(A)

if __name__ == '__main__':
    # WA for these cases
    print Solution().removeDuplicates([1,1,1])
    print Solution().removeDuplicates([1,1,1,2,2,3])
    print Solution().removeDuplicates([1,1,1,2,2,2,3,3,3])
    print Solution().removeDuplicates([1,2,3])
    print Solution().removeDuplicates([1,1,2,2,3,3])

