from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        if k == 0:
            return res

        n = len(nums)
        sliding_window_starting_index = 0
        curr_product = 1
        for ind in range(n):
            curr_product *= nums[ind]
            while curr_product >= k and sliding_window_starting_index <= ind:
                curr_product /= nums[sliding_window_starting_index]
                sliding_window_starting_index += 1

            res += ind - sliding_window_starting_index + 1

        return res
