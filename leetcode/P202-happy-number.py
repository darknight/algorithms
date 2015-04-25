class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        happy = False
        key = []
        string = str(n)
        while True:
            total = 0
            for c in string:
                total += int(c) ** 2
            if total == 1:
                happy = True
                break
            elif total in key:
                break
            else:
                key.append(total)
                string = str(total)
        return happy

if __name__ == '__main__':
    print Solution().isHappy(19)
    print Solution().isHappy(2)
