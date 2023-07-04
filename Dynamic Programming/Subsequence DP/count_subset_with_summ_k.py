# # Method - 1 (Recursion + Memoization)
class Solution:
    def perfectSum(self, arr, n, sum):
        mod = 10**9 + 7
        dp = [[-1 for i in range(sum+1)] for j in range(n)]
        '''
        if we have to consider zero int value also, then base case changes significantly
        now if we recieve target == 0 then we wont set it as standalone base case because their might be
        zeroes after that, which if pick will increase the count
        so if we reach end of the array, then we will check if target == 0 or arr[0] == target then we return 1
        but if now the target is zero and also arr[0] is also zero, then in that case we will return 2
        because we can pick and not_pick that val still we will reach the target so we add 2 in result
        '''
        def f(i, target):
            if i == 0:
                if target == 0 and arr[0] == 0:
                    return 2
                elif target == 0 or arr[0] == target:
                    return 1
                else:
                    return 0
            
            if dp[i][target] != -1:
                return dp[i][target]
            
            not_pick = f(i-1, target)
            pick = 0
            if target>=arr[i]:
                pick = f(i-1, target - arr[i])
                
            dp[i][target] = (pick + not_pick) % mod
            return dp[i][target]
            
        return f(n-1, sum)
    
# # Method - 2 (DP)
class Solution:
    def perfectSum(self, arr, n, sum):
        mod = 10**9 + 7
        dp = [[-1 for i in range(sum+1)] for j in range(n)]
        
        # handling -> target == 0
        dp[0][0] = 1
            
        '''Handling this base case
        arr[0] == target
        '''
        if sum >= arr[0]:
            dp[0][arr[0]] = 1
        
        '''Handling this base case
        if target == 0 and arr[0] == 0:
                    return 2
        '''
        if arr[0] == 0:
            dp[arr[0]][0] = 2
            
        for i in range(1,n):
            for j in range(sum+1):
                not_pick = dp[i-1][j]
                
                pick = 0
                if j>=arr[i]:
                    pick = dp[i-1][j-arr[i]]
                
                dp[i][j] = (pick + not_pick) % mod
                
        return dp[n-1][sum]
    
# # Method - 3 (Space Optimization)
class Solution:
    def perfectSum(self, arr, n, sum):
        mod = 10**9 + 7
        
        prev = [0 for i in range(sum+1)]
        
        prev[0] = 1
        if sum >= arr[0]:
            prev[arr[0]] = 1
            
        if arr[0] == 0:
            prev[0] = 2
            
        for i in range(1,n):
            curr = [0 for r in range(sum+1)] 
            for j in range(sum+1):
                not_pick = prev[j]
                
                pick = 0
                if j>=arr[i]:
                    pick = prev[j-arr[i]]
                
                curr[j] = (pick + not_pick) % mod
            prev = curr
            
        return prev[sum]