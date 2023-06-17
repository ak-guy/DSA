# # Method - 1 (Recursion)
class Solution:
    def minimizeCost(self, h, n, k):
        def f(i):
            if i == 0:
                return 0
                
            res = 1e7
            
            for j in range(1, k+1):
                if i >= j: # we can make j jumps only if we stand at index j or at an index greater than j
                    step = f(i-j) + abs(h[i]-h[i-j])
                    res = min(res, step)

            return res
            
        return f(n-1)


# # Method - 2 (Recursion + Memoization)(top down)
class Solution:
    def minimizeCost(self, h, n, k):
        dp = [-1] * n
        def f(i):
            if i == 0:
                return 0
            if dp[i] != -1:
                return dp[i]
            
            res = 1e7
            
            for j in range(1, k+1):
                if i >= j: # we can make j jumps only if we stand at index j or at an index greater than j
                    step = f(i-j) + abs(h[i]-h[i-j])
                    res = min(res, step)
            dp[i] = res
            return dp[i]
            
        return f(n-1)
    
# # Method - 3 (DP)(Tabulation)(bottom up)
class Solution:
    def minimizeCost(self, h, n, k):
        dp = [-1] * n
        dp[0] = 0
        
        for ind in range(1, n):
            res = 1e7
            for j in range(1, k+1):
                if ind >= j:
                    step = dp[ind-j] + abs(h[ind]-h[ind-j])
                    res = min(res, step)
            dp[ind] = res
            
        return dp[n-1]
    
# # Method - 4 (DP)(Space Optimization)
'''
we can at max space optimize it to O(k) and carry a list of all variable in that, but in worst case..ie k = n at
that time space complexity will become O(N)
'''