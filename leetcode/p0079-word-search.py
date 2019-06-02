#!/usr/bin/env python3

class Solution(object):
    from typing import List
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False
        visited = []
        for _ in range(m):
            visited.append([0] * n)

        for i in range(m):
            for j in range(n):
                if self.dfs(board, visited, i, j, 0, word) is True:
                    return True
        return False

    def dfs(self, board: List[List[str]], visited: List[List[str]], i: int, j: int, k: int, word: str) -> bool:
        if k == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return False
        if visited[i][j] == 1:
            return False
        if board[i][j] != word[k]:
            return False
        # match next char
        visited[i][j] = 1
        res = self.dfs(board, visited, i+1, j, k+1, word) or \
              self.dfs(board, visited, i-1, j, k+1, word) or \
              self.dfs(board, visited, i, j+1, k+1, word) or \
              self.dfs(board, visited, i, j-1, k+1, word)
        visited[i][j] = 0
        return res

if __name__ == '__main__':
    assert Solution().exist([
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ], 'ABCCED') is True
    assert Solution().exist([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], 'SEE') is True
    assert Solution().exist([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], 'ABCB') is False