class Solution:
    # @param {character[][]} board
    # @return {boolean}
    # TODO: slow, improve it
    def isValidSudoku(self, board):
        for i in range(9):
            occur = []
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in occur:
                        return False
                    occur.append(board[i][j])

        for j in range(9):
            occur = []
            for i in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in occur:
                        return False
                    occur.append(board[i][j])

        for k in range(9):
            occur = []
            for i in range(3):
                for j in range(3):
                    row = i + k / 3 * 3
                    col = j + k % 3 * 3
                    print row, col
                    if board[row][col].isdigit():
                        if board[row][col] in occur:
                            return False
                        occur.append(board[row][col])

        return True

if __name__ == '__main__':
    print Solution().isValidSudoku([
            ['5','3','.','.','7','.','.','.','.'],
            ['6','.','.','1','9','5','.','.','.'],
            ['.','9','8','.','.','.','.','6','.'],
            ['8','.','.','.','6','.','.','.','3'],
            ['4','.','.','8','.','3','.','.','1'],
            ['7','.','.','.','2','.','.','.','6'],
            ['.','6','.','.','.','.','2','8','.'],
            ['.','.','.','4','1','9','.','.','5'],
            ['.','.','.','.','8','.','.','7','9'],
        ])
