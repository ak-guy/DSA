# # Method - 1 (Recursion + Memoization)
class Solution:
    def isPalindrome(self, start, end, s):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [-1 for i in range(n)]
        def f(ind):
            # base case
            if ind == n:
                return 0
            
            if dp[ind] != -1:
                return dp[ind]

            res = 10**7
            for j in range(ind,n):
                if self.isPalindrome(ind, j, s):
                    partition = 1 + f(j+1)
                    res = min(res , partition)
            dp[ind] = res
            return dp[ind]
        
        return f(0) - 1
    
# # Method - 2 (DP)
class Solution:
    def isPalindrome(self, start, end, s):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [0 for i in range(n+1)]

        for ind in range(n-1,-1,-1):
            res = 10**7
            for j in range(ind,n):
                if self.isPalindrome(ind, j, s):
                    partition = 1 + dp[j+1]
                    res = min(res, partition)
                    
            dp[ind] = res
        
        return dp[0] - 1

'''
Giving TLE on Leetcode (n <= 2000) but runs fine on GFG (n <= 500)
'''

# # Method - 2 (DP) (Not giving TLE on Leetcode)
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [0 for i in range(n+1)]
        pal_dp = [[0 for i in range(n)] for j in range(n)]

        # preprocessing string to get all palindromes (n^2) -> it is complicated so, try to understand if you cant then move on
        for i in range(n):
            pal_dp[i][i] = True
        for i in range(n-1):
            if s[i] == s[i+1]:
                pal_dp[i][i+1] = 1
        for l in range(3, n+1):
            for i in range(n-l+1):
                j = i+l-1
                if s[i] == s[j] and pal_dp[i+1][j-1]:
                    pal_dp[i][j] = 1


        for ind in range(n-1,-1,-1):
            res = 10**7
            for j in range(ind,n):
                if pal_dp[ind][j] != 0:
                    partition = 1+dp[j+1]
                    res = min(res, partition)
                    
            dp[ind] = res
        
        return dp[0] - 1