'''
2134. Minimum Swaps to Group All 1's Together II
'''

from typing import List
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        windowSize = nums.count(1)
        count1 = nums[:windowSize].count(1)
        windowStart = 0
        windowEnd = windowSize-1
        res = windowSize-count1

        while windowStart < n:
            windowEnd = windowEnd % n
            print(windowStart, windowEnd)
            if count1 == windowSize:
                return 0

            print(count1)
            res = min(res, windowSize-count1)

            if nums[windowStart] == 1:
                count1 -= 1
            if nums[(windowEnd+1) % n] == 1:
                count1 += 1

            windowStart += 1
            windowEnd += 1
        
        return res