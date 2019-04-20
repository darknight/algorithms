#!/usr/bin/env python3

class Solution(object):
    def _multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # cheat solution
        return str(int(num1) * int(num2))

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = n2 = 0
        neg1 = neg2 = False
        if num1.startswith('-'):
            neg1 = True
            num1 = num1[1:]
        for c in num1:
            n1 = n1 * 10 + int(c)

        if num2.startswith('-'):
            neg2 = True
            num2 = num2[1:]
        for c in num2:
            n2 = n2 * 10 + int(c)

        n = n1 * n2
        neg = neg1 ^ neg2
        n = str(n)
        return '-' + n if neg else n

if __name__ == '__main__':
    print(Solution().multiply('1231', '-234523'))
