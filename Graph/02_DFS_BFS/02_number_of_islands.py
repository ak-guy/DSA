from __future__ import annotations

from collections import deque
from typing import List

"""
BFS :
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        number_of_islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                    for direction in directions:
                        new_row = row + direction[0]
                        new_col = col + direction[1]
                        if (
                            0 <= new_row < n
                            and 0 <= new_col < m
                            and grid[new_row][new_col] == "1"
                        ):
                            grid[new_row][new_col] = "X"
                            q.append((new_row, new_col))
            return True

        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1" and bfs(r, c):
                    number_of_islands += 1

        return number_of_islands


"""
DFS :
"""


class Solution:
    def dfsTraversal(
        self, r: int, c: int, grid: list[list[str]], n: int, m: int
    ) -> None:
        # base condition
        if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] != "1":
            return

        grid[r][c] = "X"
        to_traverse = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        for i in range(4):
            row = r + to_traverse[i][0]
            col = c + to_traverse[i][1]
            self.dfsTraversal(row, col, grid, n, m)

    def numIslands(self, grid: list[list[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        island_count = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    self.dfsTraversal(r, c, grid, n, m)
                    island_count += 1

        return island_count
