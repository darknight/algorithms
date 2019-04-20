class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        x2 = abs(x)
        y = x2 % 10
        x2 /= 10
        while x2 > 0:
            y = y * 10 + x2 % 10
            x2 /= 10
        return y == x

if __name__ == '__main__':
    print Solution().isPalindrome(-1)
    print Solution().isPalindrome(9)
    print Solution().isPalindrome(15)
    print Solution().isPalindrome(66)
    print Solution().isPalindrome(111)
