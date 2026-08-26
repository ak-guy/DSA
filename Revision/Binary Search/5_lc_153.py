'''
153. Find Minimum in Rotated Sorted Array

Intuition: The intuition behind this binary search is that by comparing the middle element directly 
to the rightmost boundary, we can reliably deduce which half of the rotated array contains the 
"drop-off" point where the minimum value lives. If nums[mid] is strictly greater than nums[end], 
the ascending sequence must break somewhere in the right half, meaning the smallest element is 
definitely to the right of mid, so we confidently move our start pointer to mid + 1. Conversely, 
if nums[mid] is less than or equal to nums[end], the right half is perfectly sorted and unbroken, 
which implies that the minimum value must either be at mid itself or hiding somewhere to its left, 
so we pull our end pointer down to mid. By continuously discarding the predictable half and trapping 
the pivot point within our boundaries, the search space organically shrinks until start and end 
converge directly onto the absolute minimum element.
'''

class Solution:
    def findMin(self, nums: list[int]) -> int:
        start, end = 0, len(nums)-1
        while start < end:
            mid = (start + end) // 2

            if nums[mid] > nums[end]:
                start = mid+1
            else:
                end = mid
            
        return nums[start]
