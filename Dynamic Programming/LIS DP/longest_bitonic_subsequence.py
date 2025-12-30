class Solution:
    def LongestBitonicSequence(self, nums):
        n = len(nums)
        inc_dp = [
            1 for i in range(n)
        ]  # for a particular index, it will store LIS from 0th to ith index
        inc_rev_dp = [
            1 for i in range(n)
        ]  # for a particular index, it will store LIS from (n-1)th to ith index

        res = 1

        for i in range(n):
            for j in range(0, i):
                if nums[i] > nums[j] and inc_dp[i] < 1 + inc_dp[j]:
                    inc_dp[i] = 1 + inc_dp[j]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j] and inc_rev_dp[i] < 1 + inc_rev_dp[j]:
                    inc_rev_dp[i] = 1 + inc_rev_dp[j]

        for i in range(n):
            res = max(res, inc_dp[i] + inc_rev_dp[i] - 1)

        return res
