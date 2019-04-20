class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #TODO: follow up
        if n == 1:
            return True
        elif n >= 3:
            if n % 3 != 0:
                return False
            return self.isPowerOfThree(n/3)
        return False

if __name__ == '__main__':
    print Solution().isPowerOfThree(0)
    print Solution().isPowerOfThree(1)
    print Solution().isPowerOfThree(2)
    print Solution().isPowerOfThree(3)
    print Solution().isPowerOfThree(27)
    print Solution().isPowerOfThree(56)
