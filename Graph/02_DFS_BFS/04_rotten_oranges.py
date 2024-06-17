from collections import deque
from typing import List

'''
BFS : 
'''
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
    

'''
DFS : 
'''
class Solution:
    def dfs(self, r: int, c: int, grid: List[List[int]], n: int, m: int, time_elapsed: int) -> None:
        # base_condition
        if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == 0 or time_elapsed > grid[r][c] >= 2:
            return

        grid[r][c] = time_elapsed
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        for i in range(4):
            row = r + directions[i][0]
            col = c + directions[i][1]
            self.dfs(row, col, grid, n, m, time_elapsed+1)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Algo : we will use dfs to mark every fresh orange with the time_elapsed,
        now that value will show how much time it will take to for that orange to
        rot, but we need to keep in mind that there can be multiple rotten oranges
        and we can initiate dfs only for one rotten orange at a time. So to overcome
        this we will put min of time_elapsed value in grid[r][c], this cond -> 
        time_elapsed > grid[r][c] >= 2 will ensure that.
        
        '''
        n = len(grid)
        m = len(grid[0])

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    self.dfs(r, c, grid, n, m, 2)
        
        res = 0
        for r in range(n):
            for c in range(m):
                res = max(res, grid[r][c])
                if grid[r][c] == 1:
                    return -1

        return res-2 if res > 1 else 0