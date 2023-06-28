# # Method - 1 (Recursion + Memoization)
class Solution:
    def solve(self, n, m, grid):
        dp = [[[-1 for i in range(m)] for j in range(m)] for k in range(n)]
        
        def f(r, c1, c2):
            # edge case (going out of bound)    
            if c1<0 or c2<0 or c1>m-1 or c2>m-1:
                return -(10**5)
                
            # base case
            if r == n-1:
                if c1 == c2:
                    return grid[n-1][c1]
                else:
                    return grid[n-1][c1] + grid[n-1][c2]
                    
            if dp[r][c1][c2] != -1:
                return dp[r][c1][c2]
                
            res = -(10**5)
            for col1 in range(3):
                for col2 in range(3):
                    if c1 == c2:
                        val = grid[r][c1]
                    else:
                        val = grid[r][c1] + grid[r][c2]
                        
                    dc1 = c1+col1-1
                    dc2 = c2+col2-1
                    
                    val += f(r+1, dc1, dc2)
                    res = max(res, val)
                dp[r][c1][c2] = res
            
            return dp[r][c1][c2]
            
        return f(0,0,m-1)