"""
712. Minimum ASCII Delete Sum for Two Strings
"""


class Solution:
    def getMinimumSum(self, i1, i2, s1, s2, dp):
        if i1 == len(s1) or i2 == len(s2):
            res = 0
            if i1 == len(s1):
                for i in range(i2, len(s2)):
                    res += ord(s2[i])
            else:
                for i in range(i1, len(s1)):
                    res += ord(s1[i])
            return res

        if dp[i1][i2] != -1:
            return dp[i1][i2]

        if s1[i1] == s2[i2]:
            minSum = self.getMinimumSum(i1 + 1, i2 + 1, s1, s2, dp)
        else:
            minSum = min(
                self.getMinimumSum(i1 + 1, i2, s1, s2, dp) + ord(s1[i1]),
                self.getMinimumSum(i1, i2 + 1, s1, s2, dp) + ord(s2[i2]),
            )

        dp[i1][i2] = minSum
        return dp[i1][i2]

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[-1 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        return self.getMinimumSum(0, 0, s1, s2, dp)
