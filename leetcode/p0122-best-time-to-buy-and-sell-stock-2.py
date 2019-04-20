#!/usr/bin/env python3

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
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

print(Solution().maxProfit([1,3]))
print(Solution().maxProfit([1,2,3,4,5]))
print(Solution().maxProfit([1,2,6,4,5]))
