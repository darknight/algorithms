class Solution:
    # @param prices, a list of integer
    # @return an integer
    def _maxProfit(self, prices):
        '''
        Time Limit Exceeded
        '''
        best = 0
        length = len(prices)
        for i in range(length-1):
            for j in range(i+1, length):
                best = max(best, prices[j]-prices[i])
        return best

    def maxProfit(self, prices):
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


if __name__ == '__main__':
    print Solution().maxProfit([1,2])
    print Solution().maxProfit([2,1])
    #print Solution().maxProfit([1,1,1])
    #print Solution().maxProfit([1,2,3,4,8,9,10])
    #print Solution().maxProfit([8,9,10,11,1,10,8,9])
