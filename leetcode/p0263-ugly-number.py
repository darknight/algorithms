#!/usr/bin/env python3

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num in [1, 2, 3, 5]:
            return True
        while num != 1:
            div = False
            if num % 5 == 0:
                num /= 5
                div = True
            if num % 3 == 0:
                num /= 3
                div = True
            if num % 2 == 0:
                num /= 2
                div = True
            if not div:
                return False

        return True
