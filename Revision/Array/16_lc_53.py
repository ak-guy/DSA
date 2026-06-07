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
            # "Should I continue the previous chain or start a new one?"
            if nums[i-1]>0:
                nums[i]+=nums[i-1]
                res = max(res, nums[i])
        return res



'''
Intuition: The intuition behind this alternative variation of Kadane's Algorithm treats finding the 
maximum subarray sum as a game of maximizing your profit using a Prefix Sum and Historical Minimum 
strategy. Any contiguous subarray sum can be framed as your current total accumulation (running_sum) 
minus a past accumulation from earlier in your journey. To make your current profit as large as 
possible at any given step, you want to subtract the absolute smallest, lowest valley you have ever 
dipped into since the start of the array, which you constantly keep track of using prev_min 
(seeded at 0 to represent starting fresh from the very beginning). As you march forward and collect 
numbers, you greedily calculate your potential maximum payout (running_sum - prev_min), compare it 
against your global record (res), and then immediately update your historical floor 
(prev_min = min(prev_min, running_sum)) so that future positions down the line can leverage that 
low point to maximize their own subarrays.

PS: At any point we want to maximize the (running_sum - x), hence x should be minimum
'''

class Solution2:
    def maxSubArray(self, nums: list[int]) -> int:
        res = max(nums)
        prev_min = 0
        running_sum = 0
        for num in nums:
            running_sum += num
            res = max(res, running_sum-prev_min)
            prev_min = min(prev_min, running_sum)
        return res
