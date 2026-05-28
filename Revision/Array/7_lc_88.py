'''
88. Merge Sorted Array

Intuition: The intuition for this solution lies in exploiting the empty padding at the back of nums1 to safely 
build the merged array in reverse, completely eliminating the risk of overwriting valid data before it has been 
processed. By placing a placement pointer (last_index) at the absolute end of this empty space and two tracking 
pointers (reverse_start_nums1 and reverse_start_nums2) at the backs of the active elements in both arrays, 
the algorithm works backward like a reverse countdown. It constantly compares the largest available numbers 
from both lists, copies the overall maximum to the current placement slot, and shifts the winning pointer and 
the placement pointer one step to the left. Finally, if nums2 still has remaining elements after nums1 is exhausted, 
they are simply dumped directly into the remaining front slots of nums1 since they are already guaranteed to be 
smaller than everything else successfully placed.
'''

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # we will start from the end so that we dont end up missing/overwritting
        # the values, otherwise if we start from the starting then we will overwrite
        # the values

        reverse_start_nums1 = m-1
        reverse_start_nums2 = n-1
        last_index = m+n-1

        while reverse_start_nums1 >= 0 and reverse_start_nums2 >= 0:
            if nums1[reverse_start_nums1] > nums2[reverse_start_nums2]:
                nums1[last_index] = nums1[reverse_start_nums1]
                reverse_start_nums1 -= 1
            else:
                nums1[last_index] = nums2[reverse_start_nums2]
                reverse_start_nums2 -= 1
            last_index -= 1
        
        # case where few elements from nums2 might not have traversed
        while reverse_start_nums2 >= 0:
            nums1[last_index] = nums2[reverse_start_nums2]
            reverse_start_nums2 -= 1
            last_index -= 1
