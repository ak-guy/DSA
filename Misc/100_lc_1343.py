"""
1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
"""

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currentAverage = sum(arr[:k]) / k
        startSWIndex = 1
        endSWIndex = k
        res = 0
        if currentAverage >= threshold:
            res += 1

        while endSWIndex < len(arr):
            currentAverage = (
                currentAverage + (arr[endSWIndex] - arr[startSWIndex - 1]) / k
            )
            if currentAverage >= threshold:
                res += 1

            startSWIndex += 1
            endSWIndex += 1

        return res
