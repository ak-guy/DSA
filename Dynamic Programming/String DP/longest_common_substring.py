# # Method - 1 (Recursion) -> Dont know how to implement

# # Method - 2 (DP)
class Solution:
    def longestCommonSubstr(self, text1, text2, n, m):
        dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]

        res = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                match = 0
                if text1[i - 1] == text2[j - 1]:
                    match = 1 + dp[i - 1][j - 1]
                    dp[i][j] = match
                    res = max(res, match)
                else:
                    dp[i][j] = 0

        return res


# # Method - 2 (Space Optimization)
class Solution:
    def longestCommonSubstr(self, text1, text2, n, m):
        prev = [0 for i in range(m + 1)]

        res = 0
        for i in range(1, n + 1):
            curr = [0 for k in range(m + 1)]
            for j in range(1, m + 1):
                match = 0
                if text1[i - 1] == text2[j - 1]:
                    match = 1 + prev[j - 1]
                    curr[j] = match
                    res = max(res, match)
                else:
                    curr[j] = 0

            prev = curr

        return res
