"""
413. Arithmetic Slices
"""

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        startIndex = 0
        endIndex = 0
        n = len(nums)
        currDiff = None
        res = 0

        while endIndex < n and startIndex < n - 2:
            if currDiff is None:
                endIndex += 1
                currDiff = nums[startIndex + 1] - nums[startIndex]
                continue

            while endIndex < n - 1 and nums[endIndex] + currDiff == nums[endIndex + 1]:
                endIndex += 1

            subarrayLength = endIndex - startIndex + 1
            if (subarrayLength) >= 3:
                res += (subarrayLength - 1) * (subarrayLength - 2) // 2

            startIndex = endIndex
            currDiff = None

        return res
