# # Method - 1 (sorting)
from typing import List
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort() # O(NlogN)
        res = 1
        l, r = 0, 0
        for i in range(len(nums)):
            if nums[r] - nums[l] <= k:
                r += 1
            else:
                l = i
                r = i+1
                res += 1
        return res