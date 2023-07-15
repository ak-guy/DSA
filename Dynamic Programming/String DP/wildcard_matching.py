# # Method - 1 (Recursion + Memoization)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [[-1 for i in range(m)] for j in range(n)]

        def f(i, j):
            # base case
            if i<0 and j<0: # if we have exhausted both strings then we return true
                return True
            if j<0 and i>=0: # if we have exhausted p string then we return false
                return False
            if i<0 and j>=0: # if we have have exhausted s string
                # in this p should contain only *
                for k in range(j+1):
                    if p[k] != '*':
                        return False
                return True

            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == p[j] or  p[j] == '?':
                dp[i][j] = f(i-1,j-1)
                return dp[i][j]

            elif s[i] != p[j] and p[j] == '*':
                dp[i][j] = f(i-1,j) or f(i,j-1)
                return dp[i][j]

            else:
                dp[i][j] = False
                return dp[i][j]

        return f(n-1,m-1)

# # Method - 2 (DP)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [[False for i in range(m+1)] for j in range(n+1)]

        # base case
        for j in range(1,m+1):
            flag = True
            for k in range(j):
                if p[k] != '*':
                    flag = False
                    break
            dp[0][j] = flag

        dp[0][0] = True

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]

                elif s[i-1] != p[j-1] and p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

                else:
                    dp[i][j] = False
                    
        return dp[n][m]