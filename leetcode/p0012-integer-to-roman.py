#!/usr/bin/env python3

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        mapping = [('M', 1000),
                   ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
                   ('XC', 90), ('L', 50), ('XL', 40), ('X', 10),
                   ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]
        res = ''
        for roman, value in mapping:
            while num >= value:
                res += roman
                num -= value
        return res

if __name__ == '__main__':
    print(Solution().intToRoman(1980))
