# # Method - 1 (Brute Force)
from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        for r in range(n - 1, 0, -1):
            for c in range(r):
                nums[c] = (nums[c] + nums[c + 1]) % 10

        return nums[0]


# # Method - 2 (Maths -> Pascal Triangle concept)
