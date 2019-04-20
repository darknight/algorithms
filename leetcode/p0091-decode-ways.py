#!/usr/bin/env python3

class Solution(object):
    def _numDecodings(self, s):
        """
        TLE...
        """
        total = [0]
        length = len(s)

        def _split(i):
            if i == length:
                total[0] += 1
            elif i == length - 1:
                if s[i] == '0':
                    return
                _split(i+1)
            else:
                a, b = s[i], s[i+1]
                if a == '0':
                    return
                else:
                    _split(i+1)
                    if a == '1':
                        _split(i+2)
                    if a == '2' and b not in ('7', '8', '9'):
                        _split(i+2)

        _split(0)
        return total[0]

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return 0
        if length == 1:
            dec = int(s[0])
            if dec == 0:
                # corner case
                return 0
            return 1
        res = [0] * length
        dec = int(s[:2])
        if dec < 10:
            # corner case
            return 0
        elif dec == 10 or dec == 20:
            res[0] = 0
            res[1] = 1
        elif 11 <= dec <= 19 or 21 <= dec <= 26:
            res[0] = 1
            res[1] = 2
        elif dec % 10 == 0:
            # corner case
            return 0
        else:
            res[0] = res[1] = 1
        for i in range(2, length):
            if s[i] == '0':
                if s[i-1:i+1] not in ('10', '20'):
                    # corner case
                    return 0
                res[i] = res[i-2]
            elif s[i-1] == '1' or s[i-1] == '2' and s[i] in ('1', '2', '3', '4', '5', '6'):
                res[i] = res[i-1] + res[i-2]
            else:
                res[i] = res[i-1]

        return res[-1]


if __name__ == '__main__':
    print(Solution().numDecodings('80'))
    print(Solution().numDecodings('00'))
    print(Solution().numDecodings('12'))
    print(Solution().numDecodings('27'))
    print(Solution().numDecodings('99'))
    print(Solution().numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")
