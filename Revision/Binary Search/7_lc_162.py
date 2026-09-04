'''
162. Find Peak Element

Intuition: The intuition behind this binary search is to visualize the array elements as a 
mountainous terrain and use the local slope to mathematically guarantee finding a summit. 
At each midpoint, the algorithm compares the current element against its immediate left and 
right neighbors. If it is taller than both, a local peak has been found. Otherwise, it 
evaluates the gradient: if the terrain is rising (nums[mid] > left_elem, implying the right
neighbor is even higher since we didn't return), we are actively climbing a hill, meaning a 
peak must exist somewhere ahead of us, so we confidently discard the left half and shift our 
start pointer forward. Conversely, if the terrain is falling, we are heading into a valley 
and a peak must exist behind us, so we discard the right half and pull our end pointer back. 
By treating the out-of-bounds edges as infinitely deep cliffs (-float("inf")), continuously 
following the upward slope ensures we will inevitably get trapped at a local maximum.
'''

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        start, end = 0, len(nums)
        while start <= end:
            mid = (start + end) // 2
            left_elem = nums[mid-1] if mid > 0 else -float("inf")
            right_elem = nums[mid+1] if mid < len(nums)-1 else -float("inf")

            if nums[mid] > left_elem and nums[mid] > right_elem:
                return mid

            if nums[mid] > left_elem:
                start = mid
            else:
                end = mid
