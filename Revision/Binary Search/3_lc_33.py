'''
33. Search in Rotated Sorted Array

Intuition: The intuition behind this modified binary search is that when you divide a rotated 
sorted array in half, at least one of the two halves will always remain perfectly sorted. 
By comparing the middle element to the outer boundaries, the algorithm first identifies which 
half (the left or the right) is strictly ascending. Once the "normal" half is found, we can 
confidently check if our target falls within its predictable numerical bounds; if the target 
is inside that sorted range, we discard the other half and narrow our search window strictly 
to the sorted side. If the target falls outside those bounds, it must be hiding in the unsorted, 
rotated half, so we discard the sorted side instead. By continually pinning down the predictable 
half and logically deducing where the target must belong, we can systematically cut the search 
space in half at every step.
'''
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            left_sorted = nums[start] <= nums[mid]
            _right_sorted = nums[mid] <= nums[end]
            if nums[mid] == target:
                return mid
            elif left_sorted:
                if nums[start] <= target <= nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if nums[end] >= target >= nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
        
        return -1
