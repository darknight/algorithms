#!/usr/bin/env python3

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12 or len(s) < 4:
            return []
        res = []
        
        def _find_next(prefix, left, depth):
            if depth > 4:
                return
            if left == '':
                if depth == 4:
                    x = '.'.join(prefix)
                    if x not in res:
                        res.append(x)
                return
            p = left[0]
            _find_next(prefix+(p,), left[1:], depth+1)
            if p != 0:
                q = left[:2]
                if q[0] != '0':
                    _find_next(prefix+(q,), left[2:], depth+1)
                    if q[0] == '1' or q[0] == '2':
                        r = left[:3]
                        if r < '256' and len(r) == 3:
                            _find_next(prefix+(r,), left[3:], depth+1)

        
        _find_next((), s, 0)
        return res

if __name__ == '__main__':
    print(Solution().restoreIpAddresses('25525511135'))
    print(Solution().restoreIpAddresses('8888'))
    print(Solution().restoreIpAddresses('0000'))
    print(Solution().restoreIpAddresses('255255255255'))
    print(Solution().restoreIpAddresses('127001'))
    print(Solution().restoreIpAddresses('19216811'))
    print(Solution().restoreIpAddresses('1052856'))
