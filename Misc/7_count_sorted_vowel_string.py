"""
DP Table :

        a   e   i   o   u
n=1     5   4   3   2   1
n=2     15  10  6   3   1
n=3     35  20  10  4   1
"""


class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [i for i in range(5, 0, -1)]

        for k in range(n - 1):
            temp = dp
            for i in range(3, -1, -1):
                temp[i] = dp[i] + temp[i + 1]
            dp = temp

        return dp[0]
