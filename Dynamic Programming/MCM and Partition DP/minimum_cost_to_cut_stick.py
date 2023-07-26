'''
n=9
cuts = [5,6,4,1,2]
mod_cuts = [0, 1,2,4,5,6, n]
               i       j
               k k k k k
'''

# # Method - 1 (Recursion + Memoization)
class Solution:
    def minCost(self, n: int, cuts) -> int:
        N = len(cuts)
        def f(i,j):
            if i>j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            res = 10**7
            for k in range(i, j+1):
                val = (cuts[j+1] - cuts[i-1]) + f(i,k-1) + f(k+1,j)
                res = min(res, val)
                dp[i][j] = res

            return dp[i][j]

        cuts = [0] + cuts + [n]
        cuts.sort()
        dp = [[-1 for i in range(N+1)] for j in range(N+1)]
        return f(1, N)
    
# # Method - 2 (DP)
class Solution:
    def minCost(self, n: int, cuts) -> int:
        N = len(cuts)

        cuts = [0] + cuts + [n]
        cuts.sort()
        dp = [[0 for i in range(N+2)] for j in range(N+2)]
        
        for i in range(N, 0, -1):
            for j in range(1,N+1):
                if i>j:
                    continue
                res = 10**7
                for k in range(i, j+1):
                    val = (cuts[j+1] - cuts[i-1]) + dp[i][k-1] + dp[k+1][j]
                    res = min(res, val)
                dp[i][j] = res
        return dp[1][N]