'''
partitioning can be done using three variable i,j, k
keep i at index 1 and j at index n-1, start moving index k from i till j-1 -> f(i,k)  :  f(k+1,j)
then these two function can represent partition 
'''

# # Method - 1 (Recursion)
class Solution:
    def matrixMultiplication(self, N, arr):
        def f(i, j):
            if i == j:
                return 0
            
            res = 10**7
                
            for k in range(i, j):
                steps = (arr[i-1] * arr[k] * arr[j]) + f(i,k) + f(k+1,j)
                res = min(res, steps)
            
            return res
            
        return f(1,N-1)

# # Method - 2 (Recursion + Memoization)
class Solution:
    def matrixMultiplication(self, N, arr):
        dp = [[-1 for i in range(N)] for j in range(N)]
        def f(i, j):
            if i == j:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            res = 10**9
                
            for k in range(i, j):
                steps = (arr[i-1] * arr[k] * arr[j]) + f(i,k) + f(k+1,j)
                res = min(res, steps)
                dp[i][j] = res
            
            return dp[i][j]
            
        return f(1,N-1)

# # Method - 3 (DP)
class Solution:
    def matrixMultiplication(self, N, arr):
        dp = [[0 for i in range(N)] for j in range(N)]
        
        for i in range(N-1, 0, -1):
            for j in range(i+1, N):
                res = 10**9
                
                for k in range(i, j):
                    steps = (arr[i-1] * arr[k] * arr[j]) + dp[i][k] + dp[k+1][j]
                    res = min(res, steps)
                
                dp[i][j] = res
        
        return dp[1][N-1]