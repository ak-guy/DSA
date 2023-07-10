# # Method - 1 (Recursion + Memoization) -> gave tle on gfg
# bottom - up
class Solution:
    def cutRod(self, price, n):
        dp = [[-1 for i in range(n+1)] for j in range(n)]
        def f(i, rem):
            if i>=n-1:
                if rem == n-1:
                    return price[i]
                return 0
                
            if dp[i][rem] != -1:
                return dp[i][rem]
                
            not_pick = f(i+1, rem)
            pick = 0
            if i<=rem:
                pick = f(i, rem-i-1) + price[i]
            
            dp[i][rem] = max(pick, not_pick)
            return dp[i][rem]
            
        return f(0,n-1)

# top - down
class Solution:
    def cutRod(self, price, n):
        dp = [[-1 for i in range(n+1)] for j in range(n)]
        def f(i, rem):
            if i==0:
                return rem * price[i]
                
            if dp[i][rem] != -1:
                return dp[i][rem]
                
            not_pick = f(i-1, rem)
            pick = 0
            if i<=rem-1:
                pick = price[i] + f(i, rem-i-1)
            
            dp[i][rem] = max(pick, not_pick)
            return dp[i][rem]
            
        return f(n-1,n)
    
# # Method - 2 (DP) -> gave tle on gfg
class Solution:
    def cutRod(self, price, n):
        dp = [[-1 for i in range(n+1)] for j in range(n)]
        
        for i in range(n+1):
            dp[0][i] = i * price[0]
        
        for i in range(1, n):
            for j in range(n+1):
                not_pick = dp[i-1][j]
                pick = 0
                if i<=j-1:
                    pick = price[i] + dp[i][j-i-1]
                    
                dp[i][j] = max(pick, not_pick)
                
        return dp[n-1][n]