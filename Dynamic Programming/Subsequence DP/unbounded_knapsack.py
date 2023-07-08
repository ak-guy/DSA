# # Method - 1 (Recursion + Memoization)
import sys
sys.setrecursionlimit(100000)
class Solution:
    def knapSack(self, n, W, val, wt):
        dp = [[-1 for i in range(W+1)] for j in range(n)]
        
        def f(i,target):
            if i == 0:
                if target >= wt[0]:
                    return (target // wt[0]) * val[0]
                return 0
                
            if dp[i][target] != -1:
                return dp[i][target]
            
            not_pick = f(i-1,target)
            pick = 0
            if target >= wt[i]:
                pick = val[i] + f(i,target-wt[i])
                
            dp[i][target] = max(pick, not_pick)
            return dp[i][target]
        
        return f(n-1,W)
    
# # Method - 2 (DP)
class Solution:
    def knapSack(self, n, W, val, wt):
        dp = [[0 for i in range(W+1)] for j in range(n)]
        
        if W>=wt[0]:
            for i in range(wt[0], W+1):
                dp[0][i] = (i // wt[0]) * val[0]
        
        for i in range(1,n):
            for j in range(W+1):
                not_pick = dp[i-1][j]
                pick = 0
                if j >= wt[i]:
                    pick = val[i] + dp[i][j-wt[i]]
                dp[i][j] = max(pick, not_pick)
        
        return dp[n-1][W]
    
# # Method - 3 (Space Optimization)
class Solution:
    def knapSack(self, n, W, val, wt):
        prev = [0 for i in range(W+1)]
        curr = [0 for i in range(W+1)]
        
        if W>=wt[0]:
            for i in range(wt[0], W+1):
                prev[i] = (i // wt[0]) * val[0]
        
        for i in range(1,n):
            for j in range(W+1):
                not_pick = prev[j]
                pick = 0
                if j >= wt[i]:
                    pick = val[i] + curr[j-wt[i]]
                curr[j] = max(pick, not_pick)
            prev = curr
        
        return prev[W]