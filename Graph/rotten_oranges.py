from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        total_time = 0
        q = deque()

        fresh_orange_count = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    fresh_orange_count += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        while q and fresh_orange_count > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                # print(f'row = {row}, col = {col}')
                directions = [[-1,0], [1,0], [0,-1], [0,1]]
                for direction in directions:
                    r = row + direction[0]
                    c = col + direction[1]
                    if r>=0 and c>=0 and r<n and c<m and grid[r][c] == 1:
                        fresh_orange_count -= 1
                        grid[r][c] = 2
                        q.append((r,c))
            total_time += 1
            # print(total_time)
        return total_time if fresh_orange_count == 0 else -1