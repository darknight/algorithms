#!/usr/bin/env python3

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        start = 0
        stop = len(A) - 1
        while True:
            while start <= stop and A[start] == 0:
                start += 1
            while start <= stop and A[stop] == 2:
                stop -= 1
            if start >= stop:
                break
            if A[start] == 2 or A[stop] == 0:
                A[start], A[stop] = A[stop], A[start]
            else:
                k = start + 1
                while k <= stop and A[k] == 1:
                    k += 1
                if k <= stop and A[k] == 0:
                    A[start] = 0
                    A[k] = 1
                elif k <= stop and A[k] == 2:
                    A[stop] = 2
                    A[k] = 1
                else:
                    break

if __name__ == '__main__':
    A = [0,0]
    Solution().sortColors(A)
    print(A)
    A = [2,1]
    Solution().sortColors(A)
    print(A)
    A = [1,0]
    Solution().sortColors(A)
    print(A)
    A = [2,0]
    Solution().sortColors(A)
    print(A)
    A = [1,2,0]
    Solution().sortColors(A)
    print(A)
    A = [1,2,0,1,2,0,2,1,2,1,0,0,0,1]
    Solution().sortColors(A)
    print(A)
    A = [2,2,2,2,2,2,0,0,0,0,0,0]
    Solution().sortColors(A)
    print(A)
    A = [2,2,2,2,2,1,1,1,1,1,1]
    Solution().sortColors(A)
    print(A)
