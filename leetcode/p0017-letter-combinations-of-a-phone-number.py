#!/usr/bin/env python3

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #TODO: slow & improve
        assert '0' not in digits and '1' not in digits
        length = len(digits)
        if length == 0:
            return []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = []

        def _combine(i, tmp):
            if i == length:
                res.append(tmp)
                return
            dig = digits[i]
            for c in mapping[dig]:
                _combine(i+1, tmp+c)

        _combine(0, '')

        return res

    from typing import List
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        group = ['']
        for digit in digits:
            letters = mapping[digit]
            new_group = group.copy()
            for _ in range(len(letters) - 1):
                new_group.extend(group.copy())
            for i in range(len(letters)):
                for j in range(len(group)):
                    index = j + i * len(group)
                    new_group[index] = new_group[index] + letters[i]
            group = new_group
        return group


if __name__ == '__main__':
    print(Solution().letterCombinations('23'))
    print(Solution().letterCombinations('259'))

