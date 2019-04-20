#!/usr/bin/env python3

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        length = len(A)
        n = 0
        i = 0
        while i < length:
            if A[i] == elem:
                n += 1
                A[i] = float('inf')
            i += 1
        i = 0
        while i < length:
            if A[i] == float('inf'):
                break
            i += 1
        j = i + 1
        while i < length and j < length:
            if A[j] != float('inf'):
                A[i] = A[j]
                i += 1
                j += 1
            else:
                j += 1
        A = A[:i]
        return length - n

if __name__ == '__main__':
    print(Solution().removeElement([], 6))
    print(Solution().removeElement([6,6,6,6], 6))
    print(Solution().removeElement([1,2,3,4,5,6], 6))
    print(Solution().removeElement([1,2,3,3,3,3], 3))
