#!/usr/bin/env python3

class Solution:
    # @return an integer
    def romanToInt(self, s):
        roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        r2i = {'M': 1000, 'D': 500, 'C': 100, 'L': 50,
                'X': 10, 'V': 5, 'I': 1}
        def partial_sum(i, j, s):
            if i >= j:
                return 0
            if i == j - 1:
                return r2i[s[i:j]]
            index = -1
            for num in roman:
                index = s.find(num, i, j)
                if index != -1:
                    break
            left = partial_sum(i, index, s)
            right = partial_sum(index + 1, j, s)
            res = r2i[s[index]] - left + right
            return res


        return partial_sum(0, len(s), s.upper())

if __name__ == '__main__':
    print(Solution().romanToInt('VIII') == 8)
    print(Solution().romanToInt('IX') == 9)
    print(Solution().romanToInt('XCIX') == 99)
    print(Solution().romanToInt('CMXCIX') == 999)
    print(Solution().romanToInt('MDCCCLXXXVIII') == 1888)
    print(Solution().romanToInt('MCMLXXVI') == 1976)
    print(Solution().romanToInt('MMMCMXCIX') == 3999)
