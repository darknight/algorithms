class Solution:
    # @param a list of integers
    # @return an integer

    # Time Limit Exceeded
    def _removeDuplicates(self, A):
        i = 1
        length = len(A)
        if length < 2:
            return length
        while i < length:
            j = i
            while j < length and A[j] == A[j-1]:
                j += 1
            step = j - i
            while j < length:
                A[j-step] = A[j]
                j += 1
            length -= step
            i += 1
        A = A[:length]
        return length

    # del, pop(), or remove() are not allowed.
    def _removeDuplicates(self, A):
        i = 1
        if len(A) < 2:
            return len(A)
        while i < len(A):
            if A[i] == A[i-1]:
                del A[i]
            else:
                i += 1
        return len(A)

    def removeDuplicates(self, A):
        '''
        error prone for some corner cases
        '''
        length = len(A)
        if length < 2:
            return length
        i = 1
        curr = A[0]
        while i < length:
            if A[i] == curr:
                A[i] = float('inf')
            else:
                curr = A[i]
            i += 1
        i = 0
        j = i + 1
        while i < length-1 and j < length:
            while j < length and A[j] == float('inf'):
                j += 1
            if j - i == 1:
                i += 1
                j += 1
                continue
            while j < length and A[j] != float('inf'):
                A[i+1] = A[j]
                i += 1
                j += 1
        A = A[:i+1]
        return len(A)

if __name__ == '__main__':
    # WA for these cases
    print Solution().removeDuplicates([1,1,1])
    print Solution().removeDuplicates([1,2,2])
    print Solution().removeDuplicates([1,1])
    print Solution().removeDuplicates([1,1,2])

