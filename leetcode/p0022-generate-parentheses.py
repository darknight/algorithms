class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def _dfs(val, idx, left, right):
            if left == 0 and right == 0:
                res.append(''.join(val))
                return
            if left == 0:
                val[idx] = ')'
                _dfs(val, idx+1, left, right-1)
            elif right == 0:
                return
            elif left > right:
                return
            else:
                val[idx] = '('
                _dfs(val, idx+1, left-1, right)
                val[idx] = ')'
                _dfs(val, idx+1, left, right-1)

        val = [''] * (n * 2)
        val[0] = '('
        _dfs(val, 1, n-1, n)

        return res

if __name__ == '__main__':
    print Solution().generateParenthesis(1)
    print Solution().generateParenthesis(2)
    print Solution().generateParenthesis(3)
    print Solution().generateParenthesis(4)
