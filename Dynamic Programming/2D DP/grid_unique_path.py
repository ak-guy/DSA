# # Method - 1 (Recursion)
class Solution:
    #Function to find total number of unique paths.
    def NumberOfPaths(self,a, b):
        
        def f(r,c):
            if r == -1 or c == -1:
                return 0
            if r == 0 and c == 0:
                return 1
            
            up = f(r-1,c)
            left = f(r,c-1)
            
            return up+left
            
            
        return f(a-1, b-1)
    
# # Method - 2 (Recursion + Memoization)
class Solution:
    #Function to find total number of unique paths.
    def NumberOfPaths(self,a, b):
        dp = [[-1 for i in range(b)] for j in range(a)]
        def f(r,c):
            # if r == -1 or c == -1:
            #     return 0
            if r == 0 and c == 0:
                return 1
            if dp[r][c] != -1:
                return dp[r][c]
            
            up = 0
            if r>0:
                up = f(r-1,c)
                
            left = 0
            if c>0:
                left = f(r,c-1)
            
            dp[r][c] = up+left
            return dp[r][c]
            
        return f(a-1, b-1)
    
# # Method - 3 (Tabulation)
class Solution:
    #Function to find total number of unique paths.
    def NumberOfPaths(self,a, b):
        dp = [[0 for i in range(b)] for j in range(a)]
        dp[0][0] = 1
        for r in range(a):
            for c in range(b):
                if r == c == 0:
                    continue
                
                up = 0
                if r>0:
                    up = dp[r-1][c]
                    
                left = 0
                if c>0:
                    left = dp[r][c-1]
                    
                dp[r][c] = up + left
        
        return dp[a-1][b-1]
    
# # Method - 4 (Space Optimization)
class Solution:
    #Function to find total number of unique paths.
    def NumberOfPaths(self,a, b):
        # dp = [[0 for i in range(b)] for j in range(a)]
        prev = [0 for i in range(b)]
        # prev[0] = 1

        for r in range(a):
            curr = [0 for i in range(b)]
            for c in range(b):
                if r == c == 0:
                    curr[0] = 1
                    continue
                
                up = 0
                if r>0:
                    up = prev[c]
                    
                left = 0
                if c>0:
                    left = curr[c-1]
                curr[c] = up + left
            prev = curr
        
        return prev[b-1]