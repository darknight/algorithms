#!/usr/bin/env python3

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        oper = ('+', '-', '*', '/')
        while tokens:
            token = tokens.pop(0)
            if token not in oper:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if token == '/':
                    #FIXME: 6 / -132 = -1, but in c++, it produces 0...
                    if op1 * op2 < 0:
                        v = -1 * (abs(op1) / abs(op2))
                    else:
                        v = op1 / op2
                elif token == '+':
                    v = op1 + op2
                elif token == '-':
                    v = op1 - op2
                else:
                    v = op1 * op2
                stack.append(v)

        return stack[0]

if __name__ == '__main__':
    print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
    print(Solution().evalRPN(["4", "13", "5", "/", "+"]))
    print(Solution().evalRPN(["3", "-4", "+"]))
    print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

