# # Method - 1 (Recursion + Memoization)
class Solution:
    def change(self, target, coins):
        N = len(coins)
        dp = [[-1 for i in range(target+1)] for j in range(N)]
        def f(i,target):
            if i == 0:
                if target == 0 or target % coins[0] == 0:
                    return 1
                return 0
                
            if dp[i][target] != -1:
                return dp[i][target]
                
            not_pick = f(i-1, target)
            pick = 0
            if target>=coins[i]:
                pick = f(i, target - coins[i])
            
            dp[i][target] = pick+not_pick
            return dp[i][target]
            
        return f(N-1, target)
    
# # Method - 2 (DP)
class Solution:
    def change(self, Sum: int, coins) -> int:
        N = len(coins)
        dp = [[0 for i in range(Sum+1)] for j in range(N)]
        
        for i in range(Sum+1):
            if i%coins[0]==0:
                dp[0][i] = 1
        
        for i in range(1,N):
            for j in range(Sum+1):
                not_pick = dp[i-1][j]
                pick = 0
                if j>=coins[i]:
                    pick = dp[i][j-coins[i]]
                dp[i][j] = pick + not_pick
        
        return dp[N-1][Sum]
    
# # Method - 3 (Space Optimization)
class Solution:
    def change(self, Sum: int, coins) -> int:
        N = len(coins)
        prev = [0 for i in range(Sum+1)]
        curr = [0 for i in range(Sum+1)]

        for i in range(Sum+1):
            if i%coins[0]==0:
                prev[i] = 1
        
        for i in range(1,N):
            for j in range(Sum+1):
                not_pick = prev[j]
                pick = 0
                if j>=coins[i]:
                    pick = curr[j-coins[i]]
                curr[j] = pick + not_pick
            prev = curr
        
        return prev[Sum]