class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        if len(s) % 2 == 1:
            return False
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if mapping[c] != stack[-1]:
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        return False

if __name__ == '__main__':
    print Solution().isValid('()[]{}')
    print Solution().isValid('()]{}')
    print Solution().isValid('(]{}')
    print Solution().isValid('{}')
    print Solution().isValid('')
