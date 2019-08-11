#!/usr/bin/env python3

class Solution:
    from typing import List
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        longest = 0
        start = 0
        while start <= len(A) - 3:
            if A[start+1] <= A[start]:
                start += 1
                continue
            peak = start + 1
            while peak < len(A) and A[peak] > A[peak - 1]:
                peak += 1
            if peak == len(A):
                break
            if A[peak] == A[peak-1]:
                start = peak
                continue
            end = peak
            while end < len(A) and A[end] < A[end-1]:
                end += 1
            longest = max(longest, end - start)
            start = end - 1

        return longest

    # TODO: any other solution?
    def longestMountain(self, A: List[int]) -> int:
        pass

if __name__ == '__main__':
    # assert Solution().longestMountain([2,1,4,7,3,2,5]) == 5
    # assert Solution().longestMountain([2,2,2]) == 0
    # assert Solution().longestMountain([0,1,2,3,4,5,4,3,2,1,0]) == 11
    assert Solution().longestMountain([875,884,239,731,723,685]) == 4