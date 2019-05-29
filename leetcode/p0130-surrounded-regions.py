#!/usr/bin/env python3

class Solution(object):
    from typing import List
    # TODO: slow, improve
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) < 3 or len(board[0]) < 3:
            return

        for i in range(1, len(board)-1):
            for j in range(1, len(board[i])-1):
                path = []
                self.dfs(i, j, board, path)
                self.flip_board(board, path)

        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == '':
                    board[i][j] = 'O'

        print(board)

    def dfs(self, i: int, j: int, board: List[List], path: List[tuple]) -> None:
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
            return
        if board[i][j] != 'O':
            return
        board[i][j] = ''
        path.append((i,j))
        self.dfs(i+1, j, board, path)
        self.dfs(i-1, j, board, path)
        self.dfs(i, j+1, board, path)
        self.dfs(i, j-1, board, path)
        return

    def flip_board(self, board: List[List], path: List[tuple]):
        if len(path) == 0:
            return
        captured = True
        for (i, j) in path:
            if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[i]) - 1:
                captured = False
                break
        if captured is True:
            for (i, j) in path:
                board[i][j] = 'X'


if __name__ == '__main__':
    assert Solution().solve([
        ['X','X','X','X'],
        ['X','O','O','X'],
        ['X','X','O','X'],
        ['X','O','X','X']]) is None
    assert Solution().solve([
        ['O', 'O', 'O'],
        ['O', 'O', 'O'],
        ['O', 'O', 'O']]) is None