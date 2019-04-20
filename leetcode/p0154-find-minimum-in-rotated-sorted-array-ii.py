#!/usr/bin/env python3

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if len(num) == 0:
            return
        ret = num[0]
        for x in num:
            if x < ret:
                ret = x
                break
        return ret

if __name__ == '__main__':
    print(Solution().findMin([4,5,6,7,7,7,0,1,2]))
    print(Solution().findMin([4,5,6,7,0,0,0,1,2]))
