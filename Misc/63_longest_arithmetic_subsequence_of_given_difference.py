from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        hmap = {} # val : longest subsequence possible till that value from 0th index
        res = 0
        
        for _, val in enumerate(arr):
            hmap[val] = 1 + hmap.get(val - difference, 0)
            res = max(res, hmap[val])

        return res