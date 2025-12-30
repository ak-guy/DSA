"""
1558. Minimum Numbers of Function Calls to Make Target Array
"""

from typing import List


# Method 1
class Solution:
    def getOpx(self, val):
        countOpx1 = 0
        countOpx2 = 0
        while val:
            if val % 2:
                countOpx1 += 1
                val -= 1
            else:
                countOpx2 += 1
                val /= 2
        return countOpx1, countOpx2

    def minOperations(self, nums: List[int]) -> int:
        opx1 = 0
        opx2 = 0

        for val in nums:
            first, second = self.getOpx(val)
            opx1 += first
            opx2 = max(opx2, second)

        return opx1 + opx2


# Method 2 - Using Bit Manipulation
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        opx1 = 0
        opx2 = 1
        for num in nums:
            currOpx2 = 0
            while num:
                opx1 += num % 2
                currOpx2 += 1
                num >>= 1
            opx2 = max(opx2, currOpx2)

        return opx1 + opx2 - 1
