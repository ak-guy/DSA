'''
283. Move Zeroes

Intuition: This solution uses a two-pointer partition approach where a placement pointer (start) hunts for the 
leftmost zero that needs to be replaced, while a scout pointer (end) surges ahead to find the next available 
non-zero element to swap into that slot. Initially, both pointers move together as long as they encounter 
non-zero elements, but the moment start lands on a zero, it stops and waits. The end pointer then leaves 
start behind, skimming past consecutive zeroes until it locates a non-zero "rescue" number; once found, 
the code swaps the elements, effectively sliding the non-zero value to the front and bubbling the zero 
toward the back. After the swap, both pointers step forward to repeat the cycle, ensuring that all non-zero 
numbers maintain their relative order while pushing the zeroes to the end of the array.
'''

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start = 0 # denotes the index which we have to switch
        end = 0 # denotes the index with which we have to switch 
        while end < n:
            if nums[start] == 0:
                while end < n and nums[end] == 0:
                    end += 1
                if end == n:
                    break
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end += 1
            else:
                start += 1
                end += 1
