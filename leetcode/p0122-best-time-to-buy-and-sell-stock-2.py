#!/usr/bin/env python3

class Solution:
    from typing import List
    # @param prices, a list of integer
    # @return an integer
    def _maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        i = 0
        j = 1
        res = 0
        prices.append(0)
        length = len(prices)
        while j < length:
            if prices[j-1] > prices[j]:
                if i < j-1:
                    res += prices[j-1] - prices[i]
                i = j
            j += 1
        return res

    # from 3rd party
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res

if __name__ == '__main__':
    assert Solution().maxProfit([7,1,5,3,6,4]) == 7
    assert Solution().maxProfit([1,2,3,4,5]) == 4
    assert Solution().maxProfit([7,6,4,3,1]) == 0
