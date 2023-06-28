# # Method - 1 (Recursion + Memoization)
class Solution:
    def maximumPath(self, n, m):
        res = 0
        dp = [[-1 for i in range(n)] for j in range(n)]
        def f(r,c):
            if c>=n or c<0:
                return -(10**5)
                
            if dp[r][c] != -1:
                return dp[r][c]
                
            if r == 0:
                return m[r][c]             
            
            up = f(r-1,c) + m[r][c]
            left = f(r-1,c-1) + m[r][c]
            right = f(r-1,c+1) + m[r][c]

            dp[r][c] = max(up, max(left, right))
            return dp[r][c]
        
        for i in range(n):
            total = f(n-1,i)
            res = max(res, total)
        
        return res
    
# # Method - 2 (DP)
class Solution:
    def maximumPath(self, n, m):
        res = 0
        dp = [[-1 for i in range(n)] for j in range(n)]
        
        # base case
        for i in range(n):
            dp[0][i] = m[0][i]
            
        # for r == 0, we have already set values in dp, so we will start from r==1
        for r in range(1,n):
            for c in range(n):
                up = dp[r-1][c] + m[r][c]
                
                left = m[r][c]
                if c>0:
                    left += dp[r-1][c-1]
                    
                
                right = m[r][c]
                if c<n-1:
                    right += dp[r-1][c+1]
                    
                dp[r][c] = max(up, max(left, right))
        
        # now we have filled our dp, so from our last row we need to pick largest value
        for i in range(n):
            total = dp[n-1][i]
            res = max(res, total)
        
        return res
    
# # Method - 3 (Space Optimization)
class Solution:
    def maximumPath(self, n, m):
        res = 0
        
        prev = [0] * n
        for i in range(n):
            prev[i] = m[0][i]
        
        for r in range(1,n):
            curr = [0] * n
            for c in range(n):
                up = prev[c] + m[r][c]
                
                left = m[r][c]
                if c>0:
                    left += prev[c-1]
                    
                right = m[r][c]
                if c<n-1:
                    right += prev[c+1]
                    
                curr[c] = max(up, max(left, right))
                
            prev = curr
        
        for i in range(n):
            total = prev[i]
            res = max(res, total)
        
        return res