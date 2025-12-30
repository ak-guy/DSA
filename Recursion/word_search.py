from typing import List


class Solution:
    def __init__(self):
        self.res = False

    def helper(self, board, r, c, word):
        def backtrack(i, row, col):
            if i == len(word):
                self.res = True
                return

            if (
                row < 0
                or row >= len(board)
                or col < 0
                or col >= len(board[0])
                or board[row][col] == "1"
            ):
                return

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for direction in directions:
                if board[row][col] == word[i]:
                    temp = board[row][col]
                    board[row][col] = "1"
                    backtrack(i + 1, row + direction[0], col + direction[1])
                    board[row][col] = temp

        backtrack(0, r, c)
        return self.res

    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        for r in range(n):
            for c in range(m):
                if board[r][c] == word[0] and self.helper(board, r, c, word):
                    return True

        return False
