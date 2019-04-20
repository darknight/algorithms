#!/usr/bin/env python3

class Solution(object):
    def _getPermutation(self, n, k):
        """
        TLE...
        """
        total = [0]
        raw = range(1, n+1)
        found = [None]
        def _permutate(list, i):
            if found[0] is not None:
                return
            if i == n-1:
                total[0] += 1
                if total[0] == k:
                    found[0] = ''.join(map(str, list))
                    return
            for j in range(i, n):
                new_list = list[:i] + [list[j]] + list[i:j] + list[j+1:]
                _permutate(new_list, i+1)

        _permutate(raw, 0)
        #print(found[0])
        return found[0]

    def getPermutation(self, n, k):
        raw = range(1, n+1)
        res = []
        k -= 1
        base = [1, 1]
        for i in range(2, n+1):
            base.append(base[-1] * i)
        while n:
            if k+1 == base[n]:
                raw.sort(reverse=True)
                res.extend(raw)
                break
            else:
                divide = k / base[n-1]
                res.append(raw[divide])
                del raw[divide]
                k = k % base[n-1]
                n -= 1

        return ''.join(map(str, res))

if __name__ == '__main__':
    Solution().getPermutation(1, 1)
    Solution().getPermutation(3, 1)
    Solution().getPermutation(3, 2)
    Solution().getPermutation(3, 3)
    Solution().getPermutation(3, 4)
    Solution().getPermutation(3, 5)
    Solution().getPermutation(3, 6)
    Solution().getPermutation(9, 54494)
    Solution().getPermutation(9, 94626)
