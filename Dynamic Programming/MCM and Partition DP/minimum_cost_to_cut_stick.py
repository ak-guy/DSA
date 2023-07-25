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