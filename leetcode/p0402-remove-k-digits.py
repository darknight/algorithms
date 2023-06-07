from typing import List

class Solution:
    def WA_removeKdigits(self, num: str, k: int) -> str:
        """
        case: 112
        """
        if len(num) == k or len(num) == 1:
            return "0"

        for _ in range(k):
            if num == "0":
                break
            if len(num) == 1:
                num = "0"
                break
            if num[0] > num[1]:
                num = num[1:]
            else:
                num = num[0] + num[2:]
            # deal with leading zero
            while len(num) > 1 and num[0] == "0":
                num = num[1:]

        return num


    def removeKdigits_official(self, num: str, k: int) -> str:
        """
        Greedy + Stack
        """
        numStack = []
        for digit in num:
            while k > 0 and len(numStack) > 0 and numStack[-1] > digit:
                numStack.pop()
                k -= 1

            numStack.append(digit)

        finalStack = numStack[:-k] if k > 0 else numStack
        res = "".join(finalStack).lstrip("0")

        return res or "0"
