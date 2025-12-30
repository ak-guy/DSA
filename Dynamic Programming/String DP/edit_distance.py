# # Method - 1 (Recursion + Memoization)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[-1 for i in range(m)] for j in range(n)]

        def f(i, j):
            # base case
            if j < 0:
                return (
                    i + 1
                )  # we will require (i+1 = 3) delete opn to convert "hor" to ""
            if i < 0:
                return (
                    j + 1
                )  # we will require (j+1 = 3) insert opn to convert "" to "hor"

            if dp[i][j] != -1:
                return dp[i][j]

            # match
            if word1[i] == word2[j]:
                dp[i][j] = f(i - 1, j - 1)
                return dp[i][j]
            # no match
            else:
                # 1+f(i,j-1) -> for inserting a char
                # 1+f(i-1,j) -> for deleting a char
                # 1+f(i-1,j-1) -> for replacing a char
                dp[i][j] = min(1 + f(i, j - 1), 1 + f(i - 1, j), 1 + f(i - 1, j - 1))
                return dp[i][j]

        return f(n - 1, m - 1)


# # Method - 2 (DP)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

        # base case
        for i in range(1, n + 1):
            dp[i][0] = i
        for i in range(1, m + 1):
            dp[0][i] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        1 + dp[i][j - 1], 1 + dp[i - 1][j], 1 + dp[i - 1][j - 1]
                    )

        return dp[n][m]


# # Method - 3 (Space Optimization)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        prev = [0 for i in range(m + 1)]

        # base case
        for i in range(m + 1):
            prev[i] = i

        for i in range(1, n + 1):
            curr = [0 for k in range(m + 1)]
            curr[0] = i
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = min(1 + curr[j - 1], 1 + prev[j], 1 + prev[j - 1])
            prev = curr

        return prev[m]
