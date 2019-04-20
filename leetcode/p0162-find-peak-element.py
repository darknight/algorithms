#!/usr/bin/env python3

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        length = len(num)
        if length == 0:
            return -1
        if length == 1:
            return 0
        num.insert(0, float('-inf'))
        num.append(float('-inf'))
        res = [-1]

        def peakElement(start, stop):
            if res[0] != -1:
                return
            if start > stop:
                return
            mid = (start + stop) / 2
            if num[mid] > num[mid-1] and num[mid] > num[mid+1]:
                res[0] = mid
                return
            peakElement(start, mid-1)
            peakElement(mid+1, stop)

        peakElement(1, length)
        return res[0] - 1

if __name__ == '__main__':
    print(Solution().findPeakElement([]))
    print(Solution().findPeakElement([1]))
    print(Solution().findPeakElement([1,2]) == 1)
    print(Solution().findPeakElement([1,2,3]) == 2)
    print(Solution().findPeakElement([1,3,1]) == 1)
    print(Solution().findPeakElement([1,2,3,4,5,1,2,3,4]) == 4)
