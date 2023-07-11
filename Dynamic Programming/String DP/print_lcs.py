# # Method - 1 (DP)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[0 for i in range(m+1)] for j in range(n+1)]

        # have already initialized the base case while creating dp array

        for i in range(1,n+1):
            for j in range(1,m+1):
                match = 0
                not_match = 0
                if text1[i-1] == text2[j-1]:
                    match = 1 + dp[i-1][j-1]
                else:
                    not_match = max(dp[i][j-1], dp[i-1][j])

                dp[i][j] = match+not_match

        s = ""

        r = n
        c = m
        while r>0 and c>0:
            if dp[r-1][c] == dp[r][c-1]:
                if dp[r][c] != 0:
                    s += text1[r-1]
                r -= 1
                c -= 1
            elif dp[r-1][c] > dp[r][c-1]:
                r -= 1
            else:
                c -= 1
        print(s[::-1])

obj = Solution()
obj.longestCommonSubsequence('abcab', 'cbab')