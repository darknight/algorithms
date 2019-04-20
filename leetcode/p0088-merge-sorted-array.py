#!/usr/bin/env python3

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        if n == 0:
            return
        if m == 0:
            for i, x in enumerate(B):
                A[i] = x
            return
        i = 0
        j = 0
        size = m
        while i < size and j < n:
            if A[i] <= B[j]:
                i += 1
                continue
            k = size
            while k > i:
                A[k] = A[k-1]
                k -= 1
            A[i] = B[j]
            size += 1
            j += 1
            i += 1
        while j < n:
            A[size] = B[j]
            size += 1
            j += 1

if __name__ == '__main__':
    Solution().merge([None], 0, [1], 1)
    Solution().merge([1], 1, [], 0)
    Solution().merge([1,None], 1, [2], 1)
    Solution().merge([3,None], 1, [2], 1)
    Solution().merge([1,3,5,None,None,None], 3, [2,4,6], 3)

