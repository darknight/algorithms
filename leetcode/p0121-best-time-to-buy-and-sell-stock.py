#!/usr/bin/env python3

class Solution:
    from typing import List
    # @param prices, a list of integer
    # @return an integer
    def maxProfit1(self, prices):
        '''
        Time Limit Exceeded
        '''
        best = 0
        length = len(prices)
        for i in range(length-1):
            for j in range(i+1, length):
                best = max(best, prices[j]-prices[i])
        return best

    def maxProfit2(self, prices):
        '''
        find index of min value when array is descending order,
        then when the array become ascending order, calculate the best profit,
        repeat this procedure
        '''
        if len(prices) <= 1:
            return 0
        min_index = 0
        length = len(prices)
        best = 0
        i = 0
        while i < length:
            while i < length-1 and prices[i] > prices[i+1]:
                i += 1
            if i != min_index and prices[i] < prices[min_index]:
                min_index = i
            j = i + 1
            while j < length-1 and prices[j+1] >= prices[j]:
                j += 1
            if j >= length:
                break
            best = max(best, prices[j]-prices[min_index])
            i = j+1
        return best

    def maxProfit3(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        best = 0
        i = 0
        while i < len(prices) - 1:
            j = i + 1
            if prices[i] >= prices[j]:
                i += 1
                continue
            while j < len(prices)  and prices[j] > prices[i]:
                best = max(best, prices[j] - prices[i])
                j += 1
            i = j
        return best

    # from 3rd party
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        best = 0
        curr_min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > curr_min:
                best = max(best, prices[i] - curr_min)
            else:
                curr_min = min(curr_min, prices[i])
        return best

    def AC_maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size <= 1:
            return 0
        curr_min = prices[0]
        res = 0
        for i in range(1, size):
            curr = prices[i] - curr_min
            res = max(res, curr)
            curr_min = min(curr_min, prices[i])

        return res

if __name__ == '__main__':
    assert Solution().maxProfit([1,2]) == 1
    assert Solution().maxProfit([2,1]) == 0
    assert Solution().maxProfit([1,1,1]) == 0
    assert Solution().maxProfit([1,2,3,4,8,9,10]) == 9
    assert Solution().maxProfit([8,9,10,11,1,10,8,9]) == 9
