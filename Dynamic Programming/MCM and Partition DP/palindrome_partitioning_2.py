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