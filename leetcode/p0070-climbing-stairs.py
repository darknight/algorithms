class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        '''
        f(n) = f(n-1) + f(n-2)
        '''
        s1 = 1
        s2 = 2
        if n <= 0:
            return 0
        if n == 1:
            return s1
        if n == 2:
            return s2
        for i in range(2, n):
            s = s1 + s2
            s1 = s2
            s2 = s
        return s2

if __name__ == '__main__':
    print Solution().climbStairs(1)
    print Solution().climbStairs(2)
    print Solution().climbStairs(3)
    print Solution().climbStairs(4)
