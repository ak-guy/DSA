from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_element = max(nums)
        sliding_window_starting_index = 0
        result = 0
        current_max_element_occurence = 0

        for sliding_window_ending_index in range(n):
            if nums[sliding_window_ending_index] == max_element:
                current_max_element_occurence += 1

            while sliding_window_starting_index < n and current_max_element_occurence >= k:
                if nums[sliding_window_starting_index] == max_element:
                    current_max_element_occurence -= 1
                sliding_window_starting_index += 1

            result += sliding_window_starting_index

        return result
