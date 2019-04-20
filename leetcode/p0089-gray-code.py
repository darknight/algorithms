class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        def _code(n, reverse=False):
            if n == 1:
                if reverse:
                    return [1, 0]
                else:
                    return [0, 1]
            base = 2 ** (n-1)
            left = _code(n-1)
            right = _code(n-1, reverse=True)
            if reverse:
                left = [base+i for i in left]
            else:
                right = [base+i for i in right]
            return left + right

        return _code(n)

if __name__ == '__main__':
    print Solution().grayCode(2)
    print Solution().grayCode(3)
    #print Solution().grayCode(4)
