class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        from collections import defaultdict
        bulls = 0
        cows = 0
        length = len(secret)
        smap = defaultdict(int)
        gmap = defaultdict(int)
        for i in xrange(length):
            s = secret[i]
            g = guess[i]
            if s == g:
                bulls += 1
            else:
                smap[s] += 1
                gmap[g] += 1
        for k, v in gmap.items():
            cows += min(smap[k], v)
        return '%dA%dB' % (bulls, cows)

if __name__ == '__main__':
    print Solution().getHint('1807', '7810')
    print Solution().getHint('1123', '0111')
    print Solution().getHint('1122', '2211')
