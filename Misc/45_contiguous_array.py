"""
Algo - using the concept of prefix sum we can solve this problem.
       we will maintain a hmap which will contain the total_sum mapped
       to the last index it occured, that way we know that, that sum
       occured at hmap[total_sum] ind so new resultant length can be
       i - hmap[total_sum]
"""

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum_hmap = {}  # prefix_sum : ind
        total_sum = 0
        res = 0

        for i in range(len(nums)):
            total_sum += 1 if nums[i] == 1 else -1
            if total_sum == 0:
                res = i + 1
            elif total_sum in prefix_sum_hmap:
                res = max(res, i - prefix_sum_hmap[total_sum])
            else:
                prefix_sum_hmap[total_sum] = i

        return res
