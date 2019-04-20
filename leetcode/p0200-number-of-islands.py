class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        grid.insert(0, ['0'] * (n+2))
        grid.append(['0'] * (n+2))
        for i in range(m):
            col = grid[i+1]
            col.insert(0, '0')
            col.append('0')
        def _dfs(i, j):
            if grid[i][j] == '1':
                grid[i][j] = '2'
                _dfs(i-1, j)
                _dfs(i+1, j)
                _dfs(i, j-1)
                _dfs(i, j+1)
        
        res = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if grid[i][j] == '1':
                    _dfs(i, j)
                    res += 1
        return res

if __name__ == '__main__':
    grid = [
        '1 1 0 0 0'.split(' '),
        '1 1 0 0 0'.split(' '),
        '0 0 1 0 0'.split(' '),
        '0 0 0 1 1'.split(' '),
    ]
    print Solution().numIslands(grid)
