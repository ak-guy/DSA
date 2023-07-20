class Solution:
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        dp = [1 for i in range(n)]
        hash = [1 for i in range(n)]
        nums.sort()
        count = 1

        for i in range(n):
            hash[i] = i
            for j in range(i):
                if nums[i] % nums[j] == 0 and 1+dp[j]>dp[i]:
                    hash[i] = j
                    dp[i] = 1+dp[j]
                    count = max(count, dp[i])
        
        ind = dp.index(count)
        res = []
        while ind>=0:
            if hash[ind] == ind:
                res.append(nums[ind])
                break
            res.append(nums[ind])
            ind = hash[ind]

        return res[::-1]
