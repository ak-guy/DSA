class Solution:
    def findNumberOfLIS(self, nums) -> int:
        n = len(nums)
        dp = [[1, 1] for i in range(n)]  # max_length , count

        res = 1

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i][0] < 1 + dp[j][0]:
                    dp[i][0] = 1 + dp[j][0]
                    dp[i][1] = dp[j][1]
                    res = max(res, dp[i][0])
                elif (
                    nums[i] > nums[j] and dp[i][0] == dp[j][0] + 1
                ):  # we will take all the combinations possible for index j when dp[j][0]+1 == dp[i][0]
                    dp[i][1] += dp[j][1]

        count = 0
        for i in range(n):
            if dp[i][0] == res:
                count += dp[i][1]

        return count


"""
arr = [1,2,10,6,5,4,3,7]
for this arr, 
dp = [[1, 1], [2, 1], [3, 1], [3, 1], [3, 1], [3, 1], [3, 1], [4, 4]]
"""
