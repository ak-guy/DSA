# # Method - 1 (Recursion)
class Solution:
    def isSubsetSum (self, N, arr, sum):
        
        def f(i, total):
            if total == 0:
                return True
                
            if i == 0:
                return total == arr[0] # we will consider only pick in this case because in previous not_pick is handled
            
            not_pick = f(i-1, total)
            
            pick = False
            if total >= arr[i]:
                pick = f(i-1, total - arr[i])
            
            return pick or not_pick
        
        if f(N-1, sum):
            return 1
        else:
            return 0
        
# # Method - 2 (Recursion + Memoization)
class Solution:
    def isSubsetSum (self, N, arr, sum):
        
        dp = [[-1 for i in range(sum+1)] for j in range(N)]
        def f(i, total):
            if total == 0:
                return True
                
            if i == 0:
                return total == arr[0] # we will consider only pick in this case because in previous not_pick is handled
            
            if dp[i][total] != -1:
                return dp[i][total]
            
            not_pick = f(i-1, total)
            
            pick = False
            if total >= arr[i]:
                pick = f(i-1, total - arr[i])
            
            dp[i][total] = pick or not_pick
            
            return dp[i][total]
            
        if f(N-1, sum):
            return 1
        else:
            return 0
        
# # Method - 3 (DP)
class Solution:
    def isSubsetSum (self, N, arr, sum):
        
        dp = [[0 for i in range(sum+1)] for j in range(N)]
        
        # first base case done
        for i in range(N):
            dp[i][0] = True
            
        # second base case done
        if arr[0] <= sum:
            dp[0][arr[0]] = True
        
        for i in range(1,N):
            for s in range(sum, -1, -1):
                not_pick = dp[i-1][s]
                
                pick = False
                if s>=arr[i]:
                    pick = dp[i-1][s-arr[i]]
                
                dp[i][s] = pick or not_pick
        
        if dp[N-1][sum]:
            return 1
        else:
            return 0
        
# # Method - 4 (Space Optimization)
class Solution:
    def isSubsetSum (self, N, arr, sum):
        # dp = [[0 for i in range(sum+1)] for j in range(N)]
        prev = [0 for i in range(sum+1)]
        
        # first base case done
        prev[0] = True
            
        # second base case done
        if arr[0] <= sum:
            prev[arr[0]] = True
        
        for i in range(1,N):
            curr = [0 for k in range(sum+1)] 
            for s in range(sum, -1, -1):
                not_pick = prev[s]
                
                pick = False
                if s>=arr[i]:
                    pick = prev[s-arr[i]]
                
                curr[s] = pick or not_pick
            prev = curr
        if prev[sum]:
            return 1
        else:
            return 0