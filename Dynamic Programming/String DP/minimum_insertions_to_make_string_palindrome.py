"""
we can easily find min num of insertions required if we know what is the maximum length of palindromic
subsequence that we can get from the given string, and then subtracting that length from whole length
of given string
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

        # have already initialized the base case while creating dp array

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                match = 0
                not_match = 0
                if text1[i - 1] == text2[j - 1]:
                    match = 1 + dp[i - 1][j - 1]
                else:
                    not_match = max(dp[i][j - 1], dp[i - 1][j])

                dp[i][j] = match + not_match

        return dp[n][m]

    def minInsertions(self, s: str) -> int:
        s1 = s
        s2 = s[::-1]
        l = self.longestCommonSubsequence(s1, s2)
        return len(s) - l
