from __future__ import annotations

from typing import List


class Solution:
    def getatmostKDistinctSubarray(self, nums: list[int], k: int) -> int:
        _dict = {}
        sliding_window_starting_index = 0
        res = 0
        n = len(nums)
        length_of_distinct_numbers_in_subarray_window = 0

        for ind in range(len(nums)):
            value = nums[ind]
            if value not in _dict:
                length_of_distinct_numbers_in_subarray_window += 1
            _dict[value] = 1 + _dict.get(value, 0)

            while length_of_distinct_numbers_in_subarray_window > k:
                # shrinking window from left
                _dict[nums[sliding_window_starting_index]] -= 1
                if _dict[nums[sliding_window_starting_index]] == 0:
                    _dict.pop(nums[sliding_window_starting_index])
                    length_of_distinct_numbers_in_subarray_window -= 1
                sliding_window_starting_index += 1

            res += ind - sliding_window_starting_index + 1
        return res

    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        no_of_subarray_having_atmost_k_distinct_integers = (
            self.getatmostKDistinctSubarray(
                nums,
                k,
            )
        )
        no_of_subarray_having_atmost_k_minus_1_distinct_integers = (
            self.getatmostKDistinctSubarray(
                nums,
                k - 1,
            )
        )

        return (
            no_of_subarray_having_atmost_k_distinct_integers
            - no_of_subarray_having_atmost_k_minus_1_distinct_integers
        )
