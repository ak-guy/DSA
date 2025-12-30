# # similar to https://leetcode.com/problems/count-complete-subarrays-in-an-array/
from __future__ import annotations

from typing import List


class Solution:
    def helper(self, nums, k):
        total_sum = 0
        sliding_window_starting_index = 0
        total_subarray_count = 0
        for sliding_window_ending_index in range(len(nums)):
            total_sum += nums[sliding_window_ending_index]
            while (
                total_sum > k
                and sliding_window_ending_index >= sliding_window_starting_index
            ):
                total_sum -= nums[sliding_window_starting_index]
                sliding_window_starting_index += 1
            total_subarray_count += (
                sliding_window_ending_index - sliding_window_starting_index + 1
            )

        return total_subarray_count

    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        k = goal
        getAtmostKSumSubarray = self.helper(nums, k)
        getAtmostKMinus1SumSubarray = self.helper(nums, k - 1)
        print(
            f"getAtmostKSumSubarray = {getAtmostKSumSubarray} && getAtmostKMinus1SumSubarray = {getAtmostKMinus1SumSubarray}"
        )
        return getAtmostKSumSubarray - getAtmostKMinus1SumSubarray
