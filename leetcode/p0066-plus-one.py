class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        if len(digits) == 0:
            return digits
        carry = 0
        digits[-1] += 1
        for i in range(-1, -len(digits)-1, -1):
            digits[i] = digits[i] + carry
            if digits[i] == 10:
                digits[i] = 0
                carry = 1
            else:
                carry = 0
        if carry == 1:
            digits.insert(0, 1)
        return digits

if __name__ == '__main__':
    print Solution().plusOne([])
    print Solution().plusOne([9])
    print Solution().plusOne([1,2,3,4])
    print Solution().plusOne([9,9,9])
