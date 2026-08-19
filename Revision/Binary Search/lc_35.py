'''
35. Search Insert Position

Intuition: The intuition behind this binary search approach is to pinpoint either the target's exact 
position or its correct sorted insertion index by continuously halving the search interval [start, end). 
At each step, comparing nums[mid] to target tells us which half to discard: if nums[mid] > target, 
the target must lie to the left, so we pull the upper bound down to mid; if nums[mid] < target, the 
target must lie to the right, so we push the lower bound up to mid + 1. Because moving start past any 
element smaller than target (start = mid + 1) ensures that start always tracks the count of elements 
strictly less than target, the search boundary naturally converges so that start points directly to the 
exact index where target belongs when the loop terminates.
'''

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # find upper bound value of target in nums array 
        start, end = 0, len(nums)
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid+1        
        return start
