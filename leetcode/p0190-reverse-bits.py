class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            bit = n & 0x00000001
            n = n >> 1
            res = res << 1 | bit
        return res

if __name__ == '__main__':
    print Solution().reverseBits(43261596)
