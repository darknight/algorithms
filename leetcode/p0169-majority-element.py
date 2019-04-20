#!/usr/bin/env python3

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        num.sort()
        return num[len(num) / 2]

    #TODO: quick sort
    def majorityElement2(self, num):
        pass

if __name__ == '__main__':
    print(Solution().majorityElement([1,2,3,4,5,6,5,4,1,1,1,1,1,1,1]))
