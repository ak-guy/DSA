# # Method - 1 (Recursion + Memoization)
class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        dp = [[-1 for i in range(n)] for j in range(n)]
        def f(i, j): # index at which we are at : index of last picked element
            # base case
            if i == n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
                
            not_pick = 0 + f(i+1,j)
            pick = 0
            if j ==-1 or nums[i]>nums[j]:
                pick = 1 + f(i+1,i)

            dp[i][j] = max(pick, not_pick)
            return dp[i][j]

        return f(0,-1)
    
# # Method - 2 (DP)
class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        dp = [[0 for i in range(n+1)] for j in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(i-1, -2, -1):
                not_pick = 0 + dp[i+1][j+1]
                pick = 0
                if j == -1 or nums[i]>nums[j]:
                    pick = 1 + dp[i+1][i+1]

                dp[i][j+1] = max(pick, not_pick)
                
        return dp[0][0]

# # Method - 3 (Binary Search)


