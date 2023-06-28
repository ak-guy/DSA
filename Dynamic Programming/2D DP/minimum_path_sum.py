# # Method - 1 (Recursion)
class Solution:
	def minimumCostPath(self, grid):
		n = len(grid)
		res = 10**9
		def f(r,c):
			if r==0 and c==0:
				return grid[0][0]
				
			if r<0 or c<0:
				return 10**7
			
# 			coor = [[-1,0], [0,-1]]
# 			for i in coor:
# 			    row = r+i[0]
# 			    col = c+i[1]
# 			    total = f(row,col) + grid[r][c]
# 			    res = min(total, res)

			up = f(r-1,c) + grid[r][c]
			left = f(r, c-1) + grid[r][c]
			
			return min(up, left)
			
		return f(n-1, n-1)
	
# # Method - 2 (Recursion + Memoization)
class Solution:
	def minimumCostPath(self, grid):
		n = len(grid)
		res = 10**9
		dp = [[-1 for c in range(n)] for r in range(n)]
		def f(r,c):
		#  nonlocal res
			if dp[r][c] != -1:
				return dp[r][c]
				
			if r==0 and c==0:
				return grid[0][0]
				
			if r<0 or c<0:
				return 10**7
			
# 			coor = [[-1,0], [0,-1], [0,1]]
# 			for i in coor:
# 			    row = r+i[0]
# 			    col = c+i[1]
# 			 #   print(row, col)
# 			    total = f(row,col) + grid[r][c]
# 			    res = min(total, res)

			up = f(r-1,c) + grid[r][c]
			left = f(r, c-1) + grid[r][c]
			
			dp[r][c] = min(up, left)
			return dp[r][c]
			
		return f(n-1, n-1)
	
# # Method - 3 (DP)
class Solution:
    def minimumCostPath(self, grid):
        n = len(grid)
        res = 10**9
        dp = [[-1 for c in range(n)] for r in range(n)]
        
        for r in range(n):
            for c in range(n):
                if r ==0 and c == 0:
                    dp[r][c] = grid[0][0]
                    continue
                
                up = 10**5
                if r>0:
                    up = dp[r-1][c] + grid[r][c]
                    
                left = 10**5
                if c>0:
                    left = dp[r][c-1] + grid[r][c]
                
                dp[r][c] = min(up, left)
        
        return dp[n-1][n-1]
    
# # Method - 4 (Space Optimization)
class Solution:
    def minimumCostPath(self, grid):
        n = len(grid)
        res = 10**9
        prev = [-1 for i in range(n)]
        
        # dp[0][0] = grid[0][0]
        
        for r in range(n):
            curr = [-1 for i in range(n)]
            for c in range(n):
                if r ==0 and c == 0:
                    curr[c] = grid[0][0]
                    continue
                
                up = 10**5
                if r>0:
                    up = prev[c] + grid[r][c]
                    
                left = 10**5
                if c>0:
                    left = curr[c-1] + grid[r][c]
                
                curr[c] = min(up, left)
            prev = curr
        
        return prev[n-1]