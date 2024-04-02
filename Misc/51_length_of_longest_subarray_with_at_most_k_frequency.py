from typing import List
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        count_dic = {}
        sliding_window_starting_index = 0

        for ind in range(len(nums)):
            while count_dic.get(nums[ind], 0) >= k:
                count_dic[nums[sliding_window_starting_index]] -= 1
                sliding_window_starting_index += 1

            count_dic[nums[ind]] = 1 + count_dic.get(nums[ind], 0)
            # print(count_dic) # for debugging
            res = max(res, ind - sliding_window_starting_index + 1)
        
        return res