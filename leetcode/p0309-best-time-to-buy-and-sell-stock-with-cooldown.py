class Solution(object):
    def _maxProfit(self, prices):
        """
        Time Limit Exceeded
        maximum recursion depth exceeded
        """
        length = len(prices)
        mem = [-float('inf')] * length

        def _buy(i):
            if i >= length:
                return 0
            if mem[i] > -float('inf'):
                return mem[i]
            val = _buy(i+1)
            for j in range(i+1, length):
                tmp = prices[j] - prices[i]
                tmp2 = _buy(j+2)
                val = max(val, tmp+tmp2)
            mem[i] = val
            return val

        return _buy(0)

    def __maxProfit(self, prices):
        """
        Time Limit Exceeded
        """
        length = len(prices)
        mem = [0] * (length+2)
        i = length - 2
        while i >= 0:
            if prices[i] >= prices[i+1]:
                mem[i] = mem[i+1]
            else:
                val = mem[i+1]
                for j in range(i+1, length):
                    tmp = prices[j] - prices[i]
                    tmp2 = mem[j+2]
                    val = max(val, tmp+tmp2)
                mem[i] = val
            i -= 1

        return mem[0]

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #TODO: revise
        # refer to: https://segmentfault.com/a/1190000004193861
        length = len(prices)
        if length < 2:
            return 0
        sell = [0] * length
        buy = [0] * length
        buy[0] = -prices[0]
        for i in range(1, length):
            sell[i] = max(sell[i-1], buy[i-1]+prices[i])
            if i == 2:
                buy[i] = max(buy[i-1], -prices[i])
            else:
                buy[i] = max(buy[i-1], sell[i-2]-prices[i])

        return sell[-1]

if __name__ == '__main__':
    print Solution().maxProfit([1,2,3,0,2])
    print Solution().maxProfit([3,2,6,5,0,3])
    print Solution().maxProfit([6,1,3,2,4,7])
    print Solution().maxProfit([48,12,60,93,97,42,25,64,17,56,85,93,9,48,52,42,58,85,81,84,69,36,1,54,23,15,72,15,11,94])
