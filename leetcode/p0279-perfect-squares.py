#!/usr/bin/env python3

class Solution(object):
    def numSquares1(self, n):
        """
        :type n: int
        :rtype: int
        """
        # slow solution
        data = []
        for i in range(1, n+1):
            x = i * i
            if x <= n:
                data.append(x)
            else:
                break
        data.sort(reverse=True)
        res = [n]
        def _partial(part, num, params):
            for i, d in enumerate(params):
                if part < d:
                    continue
                if part == d:
                    res[0] = min(num+1, res[0])
                    break
                if num+1 >= res[0]:
                    break
                _partial(part-d, num+1, params[i:len(params)+1])
        _partial(n, 0, data)
        return res[0]

    #
    # TLE
    #
    def numSquares2(self, n: int) -> int:
        if n <= 3:
            return n
        squares = {1}
        i = 2
        while i * i <= n:
            squares.add(i * i)
            i += 1
        queue = [n]
        visited = set()
        res = 0
        while len(queue) > 0:
            res += 1
            tmp_queue = []
            for data in queue:
                if data in squares:
                    return res
                visited.add(data)
                for i in range(1, data):
                    if i not in visited and (data - i) in squares:
                        tmp_queue.append(i)
            queue = tmp_queue

    def numSquares3(self, n: int) -> int:
        if n <= 3:
            return n
        squares = {1}
        i = 2
        while i * i <= n:
            squares.add(i * i)
            i += 1
        queue = [n]
        visited = set()
        res = 0
        while len(queue) > 0:
            res += 1
            tmp_queue = []
            for data in queue:
                if data in squares:
                    return res
                visited.add(data)
                for sq in squares:  # speed up significantly
                    child = data - sq
                    if child > 0 and child not in visited:
                        tmp_queue.append(child)
            queue = tmp_queue

    # TODO: DP
    def numSquares(self, n: int) -> int:
        pass

if __name__ == '__main__':
    assert Solution().numSquares(12) == 3
    assert Solution().numSquares(13) == 2
    assert Solution().numSquares(67) == 3
    assert Solution().numSquares(64) == 1