# # Method - 1 (Recursion + Memoization)
class Solution:
    def maxSumAfterPartitioning(self, arr, k) -> int:
        n = len(arr)
        dp = [-1 for i in range(n)]

        def f(i):
            if i == n:
                return 0
            if dp[i] != -1:
                return dp[i]

            res = -100000
            maxi = -100000
            cut = 0
            for ind in range(i, i + k):
                if ind >= n:  # will break the loop if cut exeeds n
                    break
                maxi = max(maxi, arr[ind])
                cut += 1
                ans = cut * maxi + f(ind + 1)
                res = max(res, ans)
                dp[i] = res

            return dp[i]

        return f(0)


# # Method - 2 (DP)
class Solution:
    def maxSumAfterPartitioning(self, arr, k) -> int:
        n = len(arr)
        dp = [0 for i in range(n + 1)]

        for i in range(n - 1, -1, -1):
            res = -100000
            maxi = -100000
            for cut in range(i, i + k):
                if cut >= n:
                    break
                maxi = max(maxi, arr[cut])
                ans = ((cut - i + 1) * maxi) + dp[cut + 1]
                res = max(res, ans)
            dp[i] = res

        return dp[0]
