'''
26. Remove Duplicates from Sorted Array

This code works like a production line where a placement pointer (start) stands at the first duplicate or 
"invalid" slot that needs fixing, while a scout pointer (end) races ahead to find the next uniquely 
qualified number to fill it. After initially skipping past any elements that are already in perfect, 
strictly increasing order, the code enters a hunting phase: whenever the placement slot holds an invalid 
duplicate (nums[start] <= nums[start-1]), it waits for the scout to discover a number strictly greater 
than the last successfully placed unique value (nums[end] > nums[start-1]). The moment the scout finds 
this valid number, it overwrites the duplicate at the placement slot, increments our unique count (result), 
and steps the placement pointer forward to find the next slot that needs fixing, while the scout 
continuously marches forward until the entire array has been inspected.
'''

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        result = 1
        start = 1
        end = 1
        n = len(nums)
        while start < n and nums[start-1] < nums[start]:
            start += 1
            end += 1
            result += 1

        while end < n:
            if nums[start] <= nums[start-1] and nums[end] > nums[start-1]:
                nums[start] = nums[end]
                result += 1
                start += 1
            end += 1

        return result