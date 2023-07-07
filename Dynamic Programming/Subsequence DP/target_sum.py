# # Method - 1 (Recursion + Memoization)
# same as count_subset_summ_k
class Solution:
    def findTargetSumWays(self, arr, N, target):
        # let us suppose we can divide arr in two parts => s1 + s2 = sum(arr)
        # also from problem s1 - s2 = target
        # => sum(arr) - s2 - s2 = target
        # => s2 = (sum(arr) - target) // 2
        # so we need to find how many subsets have sum s2
        
        def f(i, t):
            if i == 0:
                if arr[0] == 0 and t == 0:
                    return 2
                elif t == 0 or t == arr[0]:
                    return 1
                return 0

            if dp[i][t] != -1:
                return dp[i][t]

            not_pick = f(i-1, t)
            pick = 0
            if t>=arr[i]:
                pick = f(i-1, t-arr[i])
            
            dp[i][t] = pick + not_pick
            return dp[i][t]
        
        total = sum(arr)
        if (total - target) % 2:
            return 0
            
        if total<target:
            return 0
            
        s2 = (total - target) // 2
        dp = [[-1 for i in range(s2+1)] for j in range(N)]
        return f(N-1, s2)