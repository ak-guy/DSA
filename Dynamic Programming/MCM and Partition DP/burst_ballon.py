"""
in this problem we will start from bottom, like we will assume nums[k] is the last element we are going to pick
so after bursting it we can get coins = nums[start - 1] * nums[k] * nums[end + 1]
assuming start -> end is our search space
"""


# # Method - 1 (Recursion + Memoization)
class Solution:
    def maxCoins(self, nums) -> int:
        n = len(nums)
        nums = [1] + nums + [1]

        dp = [[-1 for i in range(n + 2)] for j in range(n + 2)]

        def f(start, end):
            if start > end:
                return 0

            if dp[start][end] != -1:
                return dp[start][end]

            res = 0
            for k in range(start, end + 1):
                val = (
                    (nums[start - 1] * nums[k] * nums[end + 1])
                    + f(start, k - 1)
                    + f(k + 1, end)
                )
                res = max(res, val)
            dp[start][end] = res

            return dp[start][end]

        return f(1, n)


# # Method - 2 (DP)
class Solution:
    def maxCoins(self, nums) -> int:
        n = len(nums)
        nums = [1] + nums + [1]

        dp = [[0 for i in range(n + 2)] for j in range(n + 2)]

        for start in range(n, 0, -1):
            for end in range(1, n + 1):
                res = 0
                for k in range(start, end + 1):
                    val = (
                        (nums[start - 1] * nums[k] * nums[end + 1])
                        + dp[start][k - 1]
                        + dp[k + 1][end]
                    )
                    res = max(res, val)
                dp[start][end] = res

        return dp[1][n]
