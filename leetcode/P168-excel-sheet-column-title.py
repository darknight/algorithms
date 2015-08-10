class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        if n <= 0:
            return ''
        start = ord('A')
        base = 26
        res = []
        while n:
            remainder = n % base
            res.insert(0, remainder)
            n = n / base
        for i in range(-1, -len(res), -1):
            if res[i] <= 0:
                res[i-1] -= 1
                res[i] += base
        if res[0] == 0:
            del res[0]
        for i in range(len(res)):
            x = res[i]
            res[i] = chr(start + x - 1)
        return ''.join(res)

if __name__ == '__main__':
    #print Solution().convertToTitle(1)
    #print Solution().convertToTitle(26)
    #print Solution().convertToTitle(27)
    #print Solution().convertToTitle(28)
    #print Solution().convertToTitle(52)
    #print Solution().convertToTitle(53)
    print Solution().convertToTitle(702)

