# # Method - 1 (Recursion + Memoization)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1 for i in range(m)] for j in range(n)]
        def f(i1, i2):
            # base case
            if i1 < 0 or i2 < 0:
                return 0

            if dp[i1][i2] != -1:
                return dp[i1][i2]

            match = 0
            not_match = 0
            if text1[i1] == text2[i2]:
                match = 1 + f(i1-1, i2-1)
            else:
                not_match = max(f(i1, i2-1), f(i1-1, i2))

            dp[i1][i2] = match+not_match
            return dp[i1][i2]

        return f(n-1, m-1)

# # Method - 2 (DP)
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
        print(*dp, sep="\n")
        return dp[n][m]
    
# # Method - 3 (Space Optimization)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        prev = [0 for i in range(m+1)]
        

        # have already initialized the base case while creating dp array

        for i in range(1,n+1):
            curr = [0 for i in range(m+1)]
            for j in range(1,m+1):
                match = 0
                not_match = 0
                if text1[i-1] == text2[j-1]:
                    match = 1 + prev[j-1]
                else:
                    not_match = max(curr[j-1], prev[j])

                curr[j] = match+not_match
            prev = curr
            
        print(curr)
        return prev[m]

obj = Solution()
print(obj.longestCommonSubsequence('abcba', 'abcbcba'))