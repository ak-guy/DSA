# # Method - 1 (Recursion)
class Solution:
    def knapSack(self, W, wt, val, n):
        def f(i, target):
            if i == 0:
                if target >= wt[0]:
                    return val[0]
                return 0

            not_pick = f(i - 1, target)
            pick = 0
            if target >= wt[i]:
                pick = val[i] + f(i - 1, target - wt[i])

            return max(pick, not_pick)

        return f(n - 1, W)


# # Method - 2 (Recursion + Memoization)
class Solution:
    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        dp = [[-1 for i in range(W + 1)] for j in range(n)]

        def f(i, target):
            if i == 0:
                if target >= wt[0]:
                    return val[0]
                return 0

            if dp[i][target] != -1:
                return dp[i][target]

            not_pick = f(i - 1, target)
            pick = 0
            if target >= wt[i]:
                pick = val[i] + f(i - 1, target - wt[i])

            dp[i][target] = max(pick, not_pick)
            return dp[i][target]

        return f(n - 1, W)


# # Method - 3 (DP)
class Solution:
    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        dp = [[0 for i in range(W + 1)] for j in range(n)]

        """
        Handling base case, if we are at index zero, then if remaining_target_weight is greater than the weight
        present at wt[0], then we can pick all weight from wt[0] till W, so we mark it in dp[0][variable]
        """
        if W >= wt[0]:
            for i in range(wt[0], W + 1):
                dp[0][i] = val[0]

        for i in range(1, n):
            for j in range(W + 1):
                not_pick = dp[i - 1][j]

                pick = 0
                if j >= wt[i]:
                    pick = val[i] + dp[i - 1][j - wt[i]]

                dp[i][j] = max(pick, not_pick)

        return dp[n - 1][W]


# # Method - 4 (Space Optimization)
class Solution:
    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        prev = [0 for i in range(W + 1)]

        if W >= wt[0]:
            for i in range(wt[0], W + 1):
                prev[i] = val[0]

        for i in range(1, n):
            curr = [0 for i in range(W + 1)]
            for j in range(W + 1):
                not_pick = prev[j]

                pick = 0
                if j >= wt[i]:
                    pick = val[i] + prev[j - wt[i]]

                curr[j] = max(pick, not_pick)
            prev = curr

        return prev[W]
