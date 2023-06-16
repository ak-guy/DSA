# # Method 1 (Brute Force)(Recursion)
class Solution:
    def minimumEnergy(self, h, n):
        # Code here
        
        def f(i):
            if i == n-1:
                return 0
            
            step1 = f(i+1) + abs(h[i]-h[i+1])
            step2 = 1e7
            if i < n-2:
                step2 = f(i+2) + abs(h[i]-h[i+2])

            return min(step1, step2)
            
        return f(0)
    

# # Method 2 (Recurion + Memoization)(top - down)

class Solution:
    def minimumEnergy(self, h, n):
        # Code here
        dp = [-1]*n
        def f(i):
            if i == 0:
                return 0
            if dp[i] != -1:
                return dp[i]
            
            step1 = f(i-1) + abs(h[i]-h[i-1])
            step2 = 1e7
            if i > 1:
                step2 = f(i-2) + abs(h[i]-h[i-2])
                
            dp[i] = min(step1, step2)
            return dp[i] 
            
        return f(n-1)
    
# # Method 3 (DP)(Tabulation)
class Solution:
    def minimumEnergy(self, h, n):
        # Code here
        dp = [-1]*n
        
        dp[0] = 0 # as previously it was set as base case, so here also setting it as 0
        
        if n == 1:
            return dp[0]
            
        for i in range(1, n):
            step1 = dp[i-1] + abs(h[i]-h[i-1])
            step2 = 1e7
            if i>1:
                step2 = dp[i-2] + abs(h[i]-h[i-2])
            
            dp[i] = min(step1, step2)
        
        return dp[n-1]
    
# # Method - 4 (DP)(Space Optimization)
class Solution:
    def minimumEnergy(self, h, n):
        # Code here
        prev1 = 0 # for i-1 (1 step jump)
        prev2 = 0 # for i-2 (2 step jump)
        
        for i in range(1, n):
            step1 = prev1 + abs(h[i]-h[i-1])
            step2 = 1e7
            if i>1:
                step2 = prev2 + abs(h[i]-h[i-2])
            
            curr = min(step1, step2)
            prev2 = prev1
            prev1 = curr
        
        return prev1