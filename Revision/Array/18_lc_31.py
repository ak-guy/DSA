'''
31. Next Permutation

Intuition: The intuition behind finding the next lexicographical permutation is to make the absolute smallest 
possible increase to the number, treating the array like a sequence of digits where we want to find the next 
highest value. To achieve this, the algorithm scans from right to left to find the very first "dip" where a 
number is smaller than its right neighbor (nums[break_point_value_ind-1] < nums[break_point_value_ind]), which 
identifies the exact position (ind_to_replace) where the increasing suffix sequence breaks and a change is 
required. If no such dip exists, it means the entire array is already in descending order 
(the absolute maximum permutation), so we simply reverse it to reset back to the absolute minimum. Once the 
breakpoint is located, the algorithm searches from the right once more to find the smallest number that is 
strictly larger than our breakpoint element, swaps them to create that minimal upward step, and then completely 
reverses the entire suffix to the right of the breakpoint. Because that suffix was guaranteed to be in descending 
order, reversing it flips it into ascending order, giving us the absolute smallest possible tail configuration 
and successfully delivering the next immediate permutation.
'''

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # take example of [1,3,3,3,4,4,2,2,2,2] and run the algorithm
        n = len(nums)
        break_point_value_ind = n-1

        while break_point_value_ind >= 0 and nums[break_point_value_ind] <= nums[break_point_value_ind-1]:
            break_point_value_ind -= 1
        
        if break_point_value_ind <= 0:
            nums.reverse()
            return
        
        ind_to_replace = break_point_value_ind-1
        ind_to_replace_with = n-1
        while nums[ind_to_replace_with] <= nums[ind_to_replace]:
            ind_to_replace_with -= 1
        
        # swap
        nums[ind_to_replace_with], nums[ind_to_replace] = nums[ind_to_replace], nums[ind_to_replace_with]

        # reverse till break_point_value_ind
        end = n-1
        while break_point_value_ind < end:
            nums[break_point_value_ind], nums[end] = nums[end], nums[break_point_value_ind]
            break_point_value_ind += 1
            end -= 1
