'''
189. Rotate Array

The intuition behind this clever three-step reversal trick relies on the realization that rotating an array by 
k steps means the last $k$ elements must wrap around to the front, while the remaining elements slide to the back. 
By flipping the entire array upside down first, you instantly move those last $k$ elements to the front half and 
push the rest to the back half—but they land facing backwards. To correct their orientation without losing their 
new positions, you simply treat the array as two independent segments (the first $k$ elements and the remaining 
n-k elements) and flip each segment back individually, restoring their original relative order. It is the 
algorithmic equivalent of turning a jacket completely inside out to move the pockets, and then rolling the 
sleeves back out right-side-up to fix them.
'''

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n

        # reverse nums
        nums.reverse()

        # reverse first k elements
        start_1, end_1 = 0, k-1
        while start_1 < end_1:
            nums[start_1], nums[end_1] = nums[end_1], nums[start_1]
            start_1 += 1
            end_1 -= 1

        # reverse last n-k elements
        start_2, end_2 = k, n-1
        while start_2 < end_2:
            nums[start_2], nums[end_2] = nums[end_2], nums[start_2]
            start_2 += 1
            end_2 -= 1
