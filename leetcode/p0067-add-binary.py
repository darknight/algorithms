#!/usr/bin/env python3

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        i2s = {0: '0', 1: '1', 2: '0', 3: '1'}
        res = []
        augend, addend = (a, b) if len(a) >= len(b) else (b, a)
        carry = 0
        for i in range(-1, -len(addend)-1, -1):
            x = int(augend[i])
            y = int(addend[i])
            z = x + y + carry
            if z == 2 or z == 3:
                carry = 1
            else:
                carry = 0
            res.insert(0, i2s[z])
        if i == -len(augend) and carry == 1:
            res.insert(0, '1')
        else:
            i -= 1
            while i != -len(augend)-1:
                if carry == 0:
                    res.insert(0, augend[i])
                else:
                    z = int(augend[i]) + carry
                    if z == 2 or z == 3:
                        carry = 1
                    else:
                        carry = 0
                    res.insert(0, i2s[z])    
                i -= 1
            if carry == 1:
                res.insert(0, '1')
        return ''.join(res)

if __name__ == '__main__':
    print(Solution().addBinary('11', '1'))
    print(Solution().addBinary('10', '10'))
    print(Solution().addBinary('111', '111'))
    print(Solution().addBinary('1111111', '1'))
    print(Solution().addBinary('10000000', '1000'))

