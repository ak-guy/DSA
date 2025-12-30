"""
1219. Path with Maximum Gold
"""

from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def backtrack(r, c):
            coinsAvailable = grid[r][c]
            res = coinsAvailable
            grid[r][c] = 0
            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

            for direction in directions:
                row = r + direction[0]
                col = c + direction[1]
                if (
                    row >= 0
                    and col >= 0
                    and row < n
                    and col < m
                    and grid[row][col] != 0
                ):
                    res = max(res, coinsAvailable + backtrack(row, col))

            # backtrack
            grid[r][c] = coinsAvailable
            return res

        n = len(grid)
        m = len(grid[0])
        res = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] != 0:
                    possibleRes = backtrack(r, c)
                    res = max(res, possibleRes)

        return res
