'''
540. Single Element in a Sorted Array

Intuition: The intuition behind this binary search approach relies on the mathematical parity of the array's 
subarrays to locate the single element. Because every other number appears exactly twice, any continuous 
segment of the array that contains only perfectly paired elements will have an even length, whereas the segment 
containing the single, isolated element will always have an odd length. At each step, the algorithm locates 
the middle element and finds its identical twin (either to its left or right), effectively splitting the 
remaining array into two distinct halves. By calculating whether the number of elements on one side of this 
pair is odd, the algorithm can instantly deduce that the single element must be hiding within that specific 
side. This allows it to safely discard the perfectly paired, even-length half and systematically zero in on 
the unique number.
'''

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        dummy_num = -1
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            left_element = nums[mid-1] if mid>0 else dummy_num
            right_element = nums[mid+1] if mid<len(nums)-1 else dummy_num

            if nums[mid] != left_element and nums[mid] != right_element:
                return nums[mid]
            
            if nums[mid] == left_element:
                if (mid-start) % 2:
                    start = mid+1
                else:
                    end = mid-2
            else:
                if (end-mid) % 2:
                    end = mid-1
                else:
                    start = mid+2

        return nums[end] # or nums[start]
