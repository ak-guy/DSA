"""
Algo : from every island (0) we will expand in all four directions
       if all four directions has water (1) then we increase the
       result by 1

Note : whenever we visit any island (0) we will mark it as 1 (water)
"""

from typing import List


class Solution:
    def checkIfClosedIsland(self, i, j, grid, n, m):
        if i < 0 or j < 0 or i >= n or j >= m:
            return False
        if grid[i][j] == 1:
            return True

        grid[i][j] = 1

        up = self.checkIfClosedIsland(i - 1, j, grid, n, m)
        left = self.checkIfClosedIsland(i, j - 1, grid, n, m)
        right = self.checkIfClosedIsland(i + 1, j, grid, n, m)
        down = self.checkIfClosedIsland(i, j + 1, grid, n, m)

        return up and left and right and down

    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        for r in range(1, n):
            for c in range(1, m):
                if grid[r][c] == 0 and self.checkIfClosedIsland(r, c, grid, n, m):
                    res += 1

        return res
