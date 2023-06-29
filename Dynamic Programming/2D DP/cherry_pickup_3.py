# # Method - 1 (Recursion + Memoization)
class Solution:
    def solve(self, n, m, grid):
        dp = [[[-1 for i in range(m)] for j in range(m)] for k in range(n)]
        
        '''
        we will assume the position of two robots as the starting point and then move accordingly
        also fuction parameter will be the location of robot (r,c1) and (r,c2), we will consider simultaneous 
        movement hence need only one parameter for row
        '''
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
            '''
            there can be nine combinations of movement if both robots have 3 option to move, so we will run 
            a double for loop and get required values
            '''
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