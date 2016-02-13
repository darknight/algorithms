class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        #TODO: too slow, improve it!
        data = []
        for i in range(1, n+1):
            x = i * i
            if x <= n:
                data.append(x)
            else:
                break
        data.sort(reverse=True)
        res = [n]
        tmp = []
        def _partial(part, num, params):
            for i, d in enumerate(params):
                if part < d:
                    continue
                if part == d:
                    #tmp.append(d)
                    #print 'bingo=>',tmp
                    #tmp.pop()
                    res[0] = min(num+1, res[0]) 
                    break
                if num+1 >= res[0]:
                    break
                #tmp.append(d)
                _partial(part-d, num+1, params[i:len(params)+1])
                #tmp.pop()
        _partial(n, 0, data)
        return res[0]

if __name__ == '__main__':
    #print Solution().numSquares(12)
    #print Solution().numSquares(13)
    #print Solution().numSquares(67)
    #print Solution().numSquares(64)
    #print Solution().numSquares(643)
    #print Solution().numSquares(7168)
    print Solution().numSquares(9975)
