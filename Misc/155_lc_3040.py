"""
3040. Maximum Number of Operations With the Same Score II
"""

"""
This solution uses a top-down dynamic programming approach with memoization 
to find the maximum number of operations performing pairs of deletions from 
either the start, the end, or one from each end while maintaining the same 
sum score for every deletion. It defines a recursive function f that, given 
a subarray defined by indices start and end and a target sum curr_val, tries 
three possible operations: deleting the first two elements, the last two 
elements, or the first and last elements if their sums match curr_val. It 
returns the maximum number of such valid operations plus one for the initial 
operation. The recursion caches results for overlapping subproblems to optimize 
performance. In the main function, it tries three initial pairs with sums from 
the first two elements, last two elements, and the first and last elements, 
recursively finding the maximum operations possible for each, and returns the 
overall maximum. This comprehensive exploration ensures the solution finds the 
maximum number of operations with the same score.
"""


class Solution:
    def f(self, start, end, nums, curr_val):
        if start >= end:
            return 0
        if self.dp[start][end] != -1:
            return self.dp[start][end]

        first_way = 0
        if nums[start] + nums[start + 1] == curr_val:
            first_way = 1 + self.f(start + 2, end, nums, curr_val)

        second_way = 0
        if nums[end] + nums[end - 1] == curr_val:
            second_way = 1 + self.f(start, end - 2, nums, curr_val)

        third_way = 0
        if nums[start] + nums[end] == curr_val:
            third_way = 1 + self.f(start + 1, end - 1, nums, curr_val)

        self.dp[start][end] = max(first_way, second_way, third_way)
        return self.dp[start][end]

    def maxOperations(self, nums: list[int]) -> int:
        n = len(nums)

        self.dp = [[-1 for _ in range(n)] for _ in range(n)]

        first_way = self.f(2, n - 1, nums, sum(nums[:2])) + 1
        second_way = self.f(0, n - 3, nums, sum(nums[n - 2 :])) + 1
        third_way = self.f(1, n - 2, nums, nums[0] + nums[-1]) + 1

        return max(first_way, second_way, third_way)
