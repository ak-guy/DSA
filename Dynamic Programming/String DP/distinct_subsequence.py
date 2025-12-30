# # Method - 1 (Recursion + Memoization)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[-1 for i in range(m)] for j in range(n)]

        def f(i, j):  # i->'s'  ;   j->'t'
            # base case
            if j < 0:
                return 1
            if i < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == t[j]:
                """
                if these two are equal then there are two cases, we can move the index in second string 
                also we need to consider the case if that val t[j] will occur again in 's'. so will take 
                both. But one thing is for sure we need to move i pointer
                """
                dp[i][j] = f(i - 1, j) + f(i - 1, j - 1)
                return dp[i][j]
            else:
                dp[i][j] = f(i - 1, j)
                return dp[i][j]

        return f(n - 1, m - 1)


# # Method - 2 (DP)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

        # base case
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, m + 1):
            dp[0][i] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][m]


# # Method - 3 (Space Optimization)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        prev = [0 for i in range(m + 1)]

        # base case
        prev[0] = 1

        for i in range(1, n + 1):
            curr = [0 for i in range(m + 1)]
            # base case
            curr[0] = 1
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    curr[j] = prev[j] + prev[j - 1]
                else:
                    curr[j] = prev[j]
            prev = curr

        return prev[m]
