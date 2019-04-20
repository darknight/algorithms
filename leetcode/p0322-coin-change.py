#!/usr/bin/env python3

class Solution(object):
    def v1coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #Time Limit Exceeded
        coins.reverse()
        res = [float('inf')]
        length = len(coins)
        tmp = []

        def _coin(idx, amount, num):
            change = coins[idx]
            n = amount / change
            while n + num >= res[0]:
                n -= 1
            while n > -1:
                reminder = amount - change * n
                if reminder == 0:
                    tmp.append(num+n)
                    res[0] = min(num+n, res[0])
                    return
                else:
                    if idx+1 < length and num+n < res[0]:
                        _coin(idx+1, reminder, num+n)
                n -= 1

        _coin(0, amount, 0)
        if res[0] < float('inf'):
            return res[0]
        return -1

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # refer to: http://www.voidcn.com/blog/qq508618087/article/p-5031191.html
        #TODO: slow & improve
        #TODO: (1)dfs, (2)bfs, (3)memorization
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for v in range(1, amount+1):
            for c in coins:
                if v >= c:
                    dp[v] = min(dp[v-c]+1, dp[v])
        if dp[amount] < float('inf'):
            return dp[amount]
        return -1

if __name__ == '__main__':
   #print(Solution().coinChange([1,2,5], 100))
   #print(Solution().coinChange([37,233,253,483], 7163))
   #print(Solution().coinChange([1,2,5], 11))
   #print(Solution().coinChange([2], 3))
   #print(Solution().coinChange([5,306,188,467,494], 7047))
   print(Solution().coinChange([70,497,443,146,392], 5695))
   #print(Solution().coinChange([1,4,5], 8))
