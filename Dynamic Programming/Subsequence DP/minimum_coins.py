# # Method - 1 (Recursion + Memoization)
class Solution:
    def coinChange(self, coins, amount):            
        n = len(coins)
        
        dp = [[-1] * (amount + 1) for i in range(n)]
        
        def f(i, target):
            if dp[i][target] != -1:
                return dp[i][target]
            
            #base case
            if i == 0:
                if target % coins[0] == 0:
                    return target // coins[0]
                else:
                    return 10**5
            
            not_take = f(i-1, target)
            take = 10**5
            if target >= coins[i]:
                take = 1 + f(i, target - coins[i])
            
            dp[i][target] = min(take, not_take)
            
            return dp[i][target]
        
        res = f(n-1, amount)
        if res >= 10**5:
            return -1
        else:
            return res
        
# # Method - 2 (DP)
class Solution:
    def coinChange(self, coins, amount):            
        n = len(coins)
        
        dp = [[10**5] * (amount + 1) for i in range(n)]
        
        for i in range(amount+1):
            if i % coins[0] == 0:
                dp[0][i] = i // coins[0]

        for i in range(1,n):
            for j in range(amount+1):

                not_take = dp[i-1][j]
                take = 10**5
                if j >= coins[i]:
                    take = 1 + dp[i][j - coins[i]]
                
                dp[i][j] = min(take, not_take)
        
        if dp[n-1][amount] != 100000:
            return dp[n-1][amount]
        else:
            return -1
        
# # Method - 3 (Space Optimization)
class Solution:
    def coinChange(self, coins, amount):            
        n = len(coins)
        
        prev = [10**5 for i in range(amount+1)]
        curr = [10**5 for i in range(amount+1)]

        for i in range(amount+1):
            if i % coins[0] == 0:
                prev[i] = i // coins[0]

        for i in range(1,n):
            for j in range(amount+1):

                not_take = prev[j]
                take = 10**5
                if j >= coins[i]:
                    take = 1 + curr[j - coins[i]]
                
                curr[j] = min(take, not_take)
            prev = curr
        
        if prev[amount] != 100000:
            return prev[amount]
        else:
            return -1