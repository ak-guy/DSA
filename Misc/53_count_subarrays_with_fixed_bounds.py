from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        '''
        consider example,
        nums: list = [3,1,2,5,2,7,1,5]
        minK: int = 1
        maxK: int = 5
        '''

        nums_length: int = len(nums)
        sliding_window_starting_index: int = 0
        result: int = 0
        found_minimum: bool = False
        found_maximum: bool = False
        ones_index: int = 0
        fives_index: int = 0

        for sliding_window_ending_index in range(nums_length):
            if nums[sliding_window_ending_index] == minK:
                found_minimum = True
                ones_index = sliding_window_ending_index
            if nums[sliding_window_ending_index] == maxK:
                found_maximum = True
                fives_index = sliding_window_ending_index

            if nums[sliding_window_ending_index] > maxK or nums[sliding_window_ending_index] < minK:
                found_minimum = False
                found_maximum = False
                sliding_window_starting_index = sliding_window_ending_index + 1
            elif found_minimum and found_maximum:
                result += (min(ones_index, fives_index) - sliding_window_starting_index + 1)

        return result
