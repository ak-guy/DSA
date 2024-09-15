from typing import List
'''
3286. Find a Safe Walk Through a Grid
'''

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        dp = [[[-1 for _ in range(health+1)] for _ in range(m)] for _ in range(n)]
        def rec(r, c, health):
            if r<0 or r==n or c<0 or c==m or health<0 or (r,c) in visited:
                return False
            if r==n-1 and c==m-1:
                if health>grid[r][c]:
                    return True
                return False

            if dp[r][c][health] != -1:
                return dp[r][c][health]        
            visited.add((r,c))
            newHealth = health-grid[r][c]
            up = rec(r-1,c,newHealth)
            down = rec(r+1,c,newHealth)
            left = rec(r,c-1,newHealth)
            right= rec(r,c+1,newHealth)
            visited.remove((r,c))
            dp[r][c][health] = up or down or left or right
            return dp[r][c][health]

        return rec(0,0,health)