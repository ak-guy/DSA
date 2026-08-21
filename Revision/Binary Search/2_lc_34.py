'''
34. Find First and Last Position of Element in Sorted Array

Intuition: The intuition behind this dual-binary search approach is that instead of stopping 
as soon as the target is found, we save the matching index and intentionally force the search 
to keep going to isolate the true outer boundaries. By passing a bias flag, whenever 
nums[mid] == target, we record mid as our best answer so far and contract the search space: 
setting end = mid - 1 with a "left" bias forces the algorithm to explore the left half for an 
even earlier occurrence, while setting start = mid + 1 with a "right" bias forces it to search 
the right half for a later occurrence. Running this directional binary search twice independently 
pinpoints the absolute first (start_ind) and last (end_ind) positions of the target in 
logarithmic time.
'''

from typing import Literal
class Solution:
    def helper(self, nums: list[int], target: int, bias: Literal["left", "right"]):
        resultant_ind = -1
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                if bias == "left":
                    end = mid-1
                else:
                    start = mid+1
                resultant_ind = mid
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid+1
        
        return resultant_ind


    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start_ind = self.helper(nums, target, "left")
        end_ind = self.helper(nums, target, "right")

        return [start_ind, end_ind]
