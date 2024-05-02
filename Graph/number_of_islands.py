from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        number_of_islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    directions = [[-1,0], [1,0], [0,1], [0,-1]]
                    for direction in directions:
                        new_row = row + direction[0]
                        new_col = col + direction[1]
                        if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] == '1':
                            grid[new_row][new_col] = 'X'
                            q.append((new_row, new_col))
            return True
            
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '1' and bfs(r,c):
                    number_of_islands += 1
            
        return number_of_islands