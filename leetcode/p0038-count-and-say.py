class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        if n < 1:
            return ''
        if n == 1:
            return '1'
        res = '1'
        while n > 1:
            n -= 1
            i = 0
            tmp = []
            while i < len(res):
                current = res[i]
                j = i + 1
                while j < len(res):
                    if res[j] == current:
                        j += 1
                    else:
                        break
                tmp.append('%s%s' % (j - i, current))
                i = j
            res = ''.join(tmp)
        return res

if __name__ == '__main__':
    print Solution().countAndSay(1)
    print Solution().countAndSay(2)
    print Solution().countAndSay(3)
    print Solution().countAndSay(4)
    print Solution().countAndSay(5)
    print Solution().countAndSay(6)
    print Solution().countAndSay(7)

