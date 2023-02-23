#!/usr/bin/env python3

from typing import List

class Solution(object):
    def AC_diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def _compute(i, j):
            if input[i:j+1].isdigit():
                return [int(input[i:j+1])]
            vals = []
            for k in range(i, j+1):
                op = input[k]
                if op in ('+', '-', '*'):
                    left = _compute(i, k-1)
                    right = _compute(k+1, j)
                    for l in left:
                        for r in right:
                            if op == '+':
                                val = l + r
                            if op == '-':
                                val = l - r
                            if op == '*':
                                val = l * r
                            vals.append(val)
            return vals

        res = _compute(0, len(input)-1)
        return res

    def diffWaysToCompute(self, expression: str) -> List[int]:
        """
        divide and conquer
        """
        def divide(exp: str) -> List[int]:
            if exp.isnumeric():
                return [int(exp)]
            res = []
            for i in range(len(exp)):
                if exp[i] in "+-*":
                    for l in divide(exp[:i]):
                        for r in divide(exp[i+1:]):
                            if exp[i] == "+":
                                res.append(l+r)
                            elif exp[i] == "-":
                                res.append(l - r)
                            else:
                                res.append(l * r)
            return res

        return divide(expression)


if __name__ == '__main__':
    print(Solution().diffWaysToCompute('2-1-1'))
    print(Solution().diffWaysToCompute('2*3-4*5'))
