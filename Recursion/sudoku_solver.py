from typing import List


class Solution:
    def isValid(self, board, r, c, i):
        for j in range(9):
            if board[r][j] == str(i): # for row condition
                return False
            if board[j][c] == str(i): # for col condition
                return False
            if board[3 * (r // 3) + (j // 3)][3 * (c // 3) + (j % 3)] == str(i): # for sub-matrix condition
                return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack(board):
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for value in range(1, 10):
                            if self.isValid(board, r, c, value):
                                board[r][c] = str(value)
                                if backtrack(board):
                                    return True
                                else:
                                    board[r][c] = '.'
                        return False
            return True

        backtrack(board)