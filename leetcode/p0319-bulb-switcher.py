class Solution(object):
    def _bulbSwitch(self, n):
        """
        Time Limit Exceeded
        """
        if n < 1:
            return 0
        if n == 1:
            return 1

        res = 0
        for k in range(1, n+1):
            if k == 1:
                res += 1
                continue
            nums = 0
            mid = (k + 1) / 2
            for i in range(2, mid+1):
                if k % i == 0:
                    nums += 1
            nums += 2
            if nums % 2 == 1:
                res += 1

        return res

    def __bulbSwitch(self, n):
        """
        Time Limit Exceeded
        """
        import math
        if n < 1:
            return 0
        if n == 1 or n == 2:
            return 1

        res = 0
        for k in range(1, n+1):
            if k == 1:
                res += 1
                continue
            if k == 2:
                continue
            nums = 0
            mid = int(math.ceil(math.sqrt(k)))
            for i in range(2, mid+1):
                if k % i == 0:
                    nums += 1
            nums += 2
            if nums % 2 == 1:
                res += 1

        return res

    def _bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        if n == 1 or n == 2:
            return 1

        res = [1] * (n+1)
        for k in range(2, n+1):
            j = k
            while j <= n:
                res[j] = res[j] ^ 1
                j += k
        return sum(res) - 1

    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        #TODO: Prove it!
        if n < 1:
            return 0
        base = 0
        step = 3
        res = 0
        while n > base:
            base += step
            step += 2
            res += 1
        return res

if __name__ == '__main__':
    for i in range(1, 38):
        print i, '=>', Solution().bulbSwitch(i)
    #print Solution().bulbSwitch(382)
    #print Solution().bulbSwitch(10000)
    #print Solution().bulbSwitch(100000)
    #print Solution().bulbSwitch(999999)
