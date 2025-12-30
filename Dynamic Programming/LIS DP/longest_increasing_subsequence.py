# # Method - 0 (brute force running two for loops)
class Solution:
    def lengthOfLIS(self, arr) -> int:
        n = len(arr)
        count = 1

        dp = [1 for i in range(n)]
        for i in range(n):
            for j in range(0, i):
                if arr[i] > arr[j] and 1 + dp[j] > dp[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    count = max(count, dp[i])

        return count


# # Method - 1 (Recursion + Memoization)
class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        dp = [[-1 for i in range(n)] for j in range(n)]

        def f(i, j):  # index at which we are at : index of last picked element
            # base case
            if i == n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            not_pick = 0 + f(i + 1, j)
            pick = 0
            if j == -1 or nums[i] > nums[j]:
                pick = 1 + f(i + 1, i)

            dp[i][j] = max(pick, not_pick)
            return dp[i][j]

        return f(0, -1)


# # Method - 2 (DP)
class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -2, -1):
                not_pick = 0 + dp[i + 1][j + 1]
                pick = 0
                if j == -1 or nums[i] > nums[j]:
                    pick = 1 + dp[i + 1][i + 1]

                dp[i][j + 1] = max(pick, not_pick)

        return dp[0][0]


# # Method - 3 (Binary Search)
class Solution:
    def lengthOfLIS(self, arr) -> int:
        res = []
        res.append(arr[0])
        count = 1
        n = len(arr)

        for i in range(1, n):
            if arr[i] > res[count - 1]:
                res.append(arr[i])
                count += 1
            else:
                ind = self.upper_bound(res, arr[i])
                if ind == -1:
                    ind = 0
                res[ind] = arr[i]

        return count

    def upper_bound(self, array, target):
        left = 0
        right = len(array) - 1

        if target > array[right]:
            return -1

        while left < right:
            mid = (left + right) // 2

            # In this case only two element will remain
            if left == mid:
                return left if array[left] >= target else left + 1

            # Usual binary search but we know if target is greater than mid-value of array then for sure result lies to the right of mid( excluding itself)
            if target == array[mid]:
                return mid
            elif target > array[mid]:
                left = mid + 1
            else:
                right = mid

        return left
