# same as Misc/34_subarray_with_k_different_integers.py
from __future__ import annotations

from typing import List


class Solution:
    def getDistinctSubarrays(self, nums: list[int], k: int) -> int:
        dummy_dict = {}
        res = 0
        window_start_index = 0
        distinct_values_in_window = 0
        for i in range(len(nums)):
            if nums[i] not in dummy_dict:
                distinct_values_in_window += 1
            dummy_dict[nums[i]] = 1 + dummy_dict.get(nums[i], 0)

            while distinct_values_in_window > k:
                dummy_dict[nums[window_start_index]] -= 1
                if dummy_dict[nums[window_start_index]] == 0:
                    dummy_dict.pop(nums[window_start_index])
                    distinct_values_in_window -= 1
                window_start_index += 1

            res += (i - window_start_index + 1)
        return res

    def countCompleteSubarrays(self, nums: list[int]) -> int:
        k = len(set(nums))
        atmost_k_distinct_subarray = self.getDistinctSubarrays(nums, k)
        atmost_k_minus_1_distinct_subarray = self.getDistinctSubarrays(
            nums, k-1)

        return atmost_k_distinct_subarray - atmost_k_minus_1_distinct_subarray
