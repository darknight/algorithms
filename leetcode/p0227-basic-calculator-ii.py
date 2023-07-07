#!/usr/bin/env python3

import math, itertools, functools, heapq
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass


class Solution:
    def calculate(self, s: str) -> int:
        num_stack = []
        op_stack = []
        i = 0
        size = len(s)
        while i < size:
            if s[i].isspace():
                i += 1
                continue
            if s[i].isdigit():
                val = 0
                j = i
                while j < size and s[j].isdigit():
                    val = val * 10 + ord(s[j]) - ord('0')
                    j += 1
                # peek op_stack
                if len(op_stack) > 0 and op_stack[-1] in ("*", "/"):
                    op = op_stack.pop()
                    left = num_stack.pop()
                    if op == "*":
                        val = left * val
                    else:
                        val = left // val
                # push stack
                num_stack.append(val)
                i = j
                continue
            else:
                if len(op_stack) > 0 and s[i] in ("+", "-"):
                    op = op_stack.pop()
                    right = num_stack.pop()
                    left = num_stack.pop()
                    if op == "+":
                        num_stack.append(left + right)
                    else:
                        num_stack.append(left - right)
                op_stack.append(s[i])
                i += 1
        if len(op_stack) > 0:
            op = op_stack.pop()
            right = num_stack.pop()
            left = num_stack.pop()
            if op == "+":
                num_stack.append(left + right)
            else:
                num_stack.append(left - right)

        return num_stack[0]

    def calculate_official(self, s: str) -> int:
        """
        a - b == a + (-b)
        a - b * c == a + (-b) * c
        a - b / c == a + (-b) * c
        so we can do sum(num_stack) in the end

        one issue:
        3 // 2 == 1
        -3 // 2 == -2
        """
        num_stack = []
        size = len(s)
        curr = 0
        op = "+"
        for i in range(size):
            if s[i].isdigit():
                curr = curr * 10 + int(s[i])
            if s[i] in ("+", "-", "*", "/") or i == size - 1:
                if op == "+":
                    num_stack.append(curr)
                elif op == "-":
                    num_stack.append(-curr)
                elif op == "*":
                    num_stack.append(num_stack.pop() * curr)
                else:
                    num_stack.append(int(num_stack.pop() / curr))
                curr = 0
                op = s[i]

        return sum(num_stack)

    def calculate_official_with_sentinel(self, s: str) -> int:
        """
        https://leetcode.com/problems/basic-calculator-ii/solutions/3227668/227-time-91-15-solution-with-step-by-step-explanation/
        """
        num_stack = []
        curr = 0
        op = "+"
        for c in s + "+":
            if c.isdigit():
                curr = curr * 10 + int(c)
            if c in ("+", "-", "*", "/"):
                if op == "+":
                    num_stack.append(curr)
                elif op == "-":
                    num_stack.append(-curr)
                elif op == "*":
                    num_stack.append(num_stack.pop() * curr)
                else:
                    num_stack.append(int(num_stack.pop() / curr))
                curr = 0
                op = c

        return sum(num_stack)


if __name__ == '__main__':
    pass
