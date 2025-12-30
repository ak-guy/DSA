from typing import List


"""
for n = 4:  (0,0)   (1,-1)   (2,-2)    (3,-3)
            (1,1)   (2, 0)   (3,-1)    (4,-2)
            (2,2)   (3, 1)   (4, 0)    (5,-1)
            (3,3)   (4, 2)   (5, 1)    (6, 0)

these are (posDiagonal, negDiagonal)
"""


class Solution:
    def __init__(self):
        self.res = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for i in range(n)] for j in range(n)]
        posDiagonal = set()  # r+c
        negDiagonal = set()  # r-c
        column = set()

        def backtrack(row):
            if row == n:
                possible_res = ["".join(row) for row in board]
                self.res.append(possible_res.copy())
                return

            for col in range(n):
                if (
                    col in column
                    or (row + col) in posDiagonal
                    or (row - col) in negDiagonal
                ):
                    continue
                posDiagonal.add(row + col)
                negDiagonal.add(row - col)
                column.add(col)
                board[row][col] = "Q"
                backtrack(row + 1)

                posDiagonal.remove(row + col)
                negDiagonal.remove(row - col)
                column.remove(col)
                board[row][col] = "."

        backtrack(0)

        return self.res
