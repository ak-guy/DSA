'''
81. Search in Rotated Sorted Array II

Intuition: The intuition behind this solution—which handles a rotated sorted array that contains 
duplicates—is that you can still rely on the predictable nature of binary search, but with a 
clever structural escape hatch to handle edge-case ambiguity. Just like in the unique-element 
version, splitting the array down the middle guarantees that at least one half will be perfectly 
sorted, allowing you to easily verify if the target falls within that sorted boundary. However, 
the introduction of duplicates introduces a major hurdle: if the values at the start, mid, and 
end pointers are all completely identical (e.g., [1, 0, 1, 1, 1]), the algorithm suddenly loses 
the ability to determine which half is the sorted one. To break this informational deadlock 
without sacrificing correctness, the algorithm deploys an intermediate cleanup step: it simply 
shrinks both outer boundaries inward by one step (start += 1 and end -= 1), shaving off the 
duplicate data while safely preserving the core search space. Once this ambiguity is cleared away, 
the algorithm resumes its standard routine of identifying the normally sorted half and halving 
the search space, maintaining highly efficient lookup capabilities across almost all inputs.
'''

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            left_sorted = nums[start] <= nums[mid]
            _right_sorted = nums[mid] <= nums[end]
            if nums[mid] == target:
                return True
            elif nums[start] == nums[mid] == nums[end]:
                start += 1
                end -= 1
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
        
        return False
