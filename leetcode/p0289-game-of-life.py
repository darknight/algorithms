class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        if n == 0:
            return

        board.insert(0, [0] * (n+2))
        board.append([0] * (n+2))
        for i in range(1, m+1):
            row = board[i]
            row.insert(0, 0)
            row.append(0)

        ops = []
        for i in range(1, m+1):
            for j in range(1, n+1):
                lives = 0
                lives += board[i-1][j-1]
                lives += board[i-1][j]
                lives += board[i-1][j+1]
                lives += board[i][j-1]
                lives += board[i][j+1]
                lives += board[i+1][j-1]
                lives += board[i+1][j]
                lives += board[i+1][j+1]
                origin = board[i][j]
                if origin == 0 and lives == 3:
                    ops.append((i, j, 1))
                elif origin == 1:
                    if lives < 2 or lives > 3:
                        ops.append((i, j, 0))

        for (i, j, val) in ops:
            board[i][j] = val
        board.pop(0)
        board.pop()
        for i in range(m):
            row = board[i]
            row.pop(0)
            row.pop()

if __name__ == '__main__':
    board = [
        [1, 0, 1],
        [0, 1, 0],
    ]
    Solution().gameOfLife(board)
