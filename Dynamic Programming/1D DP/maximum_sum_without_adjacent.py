# # Method - 1 (Recursion)
class Solution:
    def findMaxSum(self, arr, n):
        def f(i):
            if i < 0:
                return 0
            if i == 0:
                return arr[0]
            
            not_pick = f(i-1)
            pick = f(i-2) + arr[i]

            return max(pick, not_pick)
        
        return f(n-1)
    
# # Method - 2 (Recursion + Memoization)
class Solution:
    def findMaxSum(self, arr, n):
        dp = [-1] * n
        def f(i):
            if i < 0:
                return 0
            if i == 0:
                return arr[0]
            if dp[i] != -1:
                return dp[i]
                        
            not_pick = f(i-1)
            pick = f(i-2) + arr[i]

            dp[i] = max(pick, not_pick)
            return dp[i]
        
        return f(n-1)
    
# # Method - 3 (DP)(Tabulation)
class Solution:
    def findMaxSum(self, arr, n):
        dp = [0] * n
        dp[0] = arr[0]
        
        for i in range(1, n):
            pick = arr[i]
            if i>=2:
                pick += dp[i-2]
            not_pick = dp[i-1]
            
            dp[i] = max(pick, not_pick)
        
        return dp[n-1]
    
# # Method - 4 (DP)(Space Optimization)
class Solution:
    def findMaxSum(self, arr, n):
        prev = arr[0]
        prev2 = 0
        curr = 0
        for i in range(1, n):
            pick = arr[i]
            if i>=2:
                pick += prev2
            not_pick = prev
            
            curr = max(pick, not_pick)
            prev2 = prev
            prev = curr
        
        return prev