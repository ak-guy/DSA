'''
75. Sort Colors

Intuition: The intuition behind this two-pass solution is to organize the array by tackling one extreme 
color boundary at a time using a two-pointer partitioning strategy. Instead of sorting everything at once, 
the algorithm divides the work into two distinct filtering steps: the first pass acts as a magnet for zeroes, 
using a start pointer to locate non-zero intruders at the front and swapping them with zeroes found by an 
end pointer scouting from the back until all zeroes are perfectly anchored at the beginning of the array. 
Once the zeroes are locked in place, the second pass resets the pointers to filter the other extreme by hunting 
down the twos; it uses the end pointer to claim correct positions for twos at the back of the array and forces 
the start pointer to search from the front for misplaced twos to swap into those rear slots. By systematically 
pushing all zeroes to the far left and then all twos to the far right, the ones are naturally trapped and 
sorted in the middle by a simple process of elimination.
'''

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)

        # first pass, ensuring that 0 is at the starting
        start, end = 0, n-1
        while start < end:
            if nums[start] == 0:
                start += 1
            else:
                while start < end and nums[end] != 0:
                    end -= 1
                nums[start], nums[end] = nums[end], nums[start]
                start += 1

        # second pass, ensuring 2's at the end
        start, end = 0, n-1
        while start < end:
            if nums[end] == 2:
                end -= 1
            else:
                while start < end and nums[start] != 2:
                    start += 1
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1


        
'''
Intuition: The intuition behind this highly optimized single-pass solution—known as the Dutch 
National Flag algorithm—is to actively partition the array into three distinct color zones by 
using a single main scanner (mid) that routes elements to their respective boundary guards. 
You maintain a start pointer acting as the boundary for zeroes on the far left, an end pointer 
acting as the boundary for twos on the far right, and the mid pointer to inspect unclassified 
elements in the center. As mid marches forward, it acts like a sorting conveyor belt: if it 
discovers a 0, it throws it to the start boundary and both pointers step forward; if it discovers 
a 2, it throws it to the end boundary and the end boundary shrinks inward (while mid stays put 
to inspect the mystery element just swapped into its lap); and if it discovers a 1, it simply 
leaves it alone and moves on since ones naturally belong in the middle. By continuously pushing 
zeroes to the absolute left and twos to the absolute right, the ones are automatically compressed 
into the center, sorting the entire array in a single, elegant sweep.
'''

class Solution_Dutch_Flag:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # single pass, ensuring everything left to start is 0, and everything right to end is 2
        start, mid, end = 0, 0, n-1
        while mid <= end:
            if nums[mid] == 0:
                nums[start], nums[mid] = nums[mid], nums[start]
                start += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1
            else:
                mid += 1
        