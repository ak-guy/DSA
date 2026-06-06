'''
53. Maximum Subarray

Intuition: The intuition behind this solution—a clever in-place variation of Kadane's Algorithm—is 
built on the core decision of whether it is beneficial to carry over the mathematical "baggage" of 
your past choices. As you march step-by-step through the array, each element nums[i] looks back at 
the modified cumulative sum accumulated at the immediately preceding position nums[i-1]. If that 
previous neighbor is a positive number (nums[i-1] > 0), it represents a helpful head start, so the 
current element absorbs it (nums[i] += nums[i-1]) to extend the ongoing streak and maximize its 
own value. Conversely, if the previous neighbor is negative or zero, it would only drag the current 
element down, so the algorithm implicitly dumps the past and forces the current element to start a 
brand-new, independent subarray streak from its own position. By continuously overwriting each slot 
with the best possible local sum ending exactly at that index, a global tracker (res) can constantly 
scan these choices to lock in the single highest subarray sum achieved across the entire journey.
'''

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = max(nums)
        for i in range(1, len(nums)):
            if nums[i-1]>0:
                nums[i]+=nums[i-1]
                res = max(res, nums[i])
        return res
