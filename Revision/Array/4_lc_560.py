'''
560. Subarray Sum Equals K

The intuition for this solution relies on the idea that any contiguous subarray sum can be calculated by 
taking the total sum from the beginning of the array up to your current position (running_prefix_sum) and 
subtracting a previous prefix sum from earlier in your journey. If you are standing at a current total sum 
and want to know if a subarray ending at your feet equals $k$, you mathematically need to find out if you 
have ever stood at a previous total sum equal to running_prefix_sum - k. Instead of looking backward and 
recalculating past sums manually, you use a hash map (encountered_sum) as a history book that remembers 
exactly how many times every previous prefix sum has occurred. By initializing this map with {0: 1}, you 
elegantly handle the scenario where the current prefix sum itself perfectly equals $k$ right from the very 
start of the array, meaning you don't need to subtract any past subarray to hit your target. As you loop 
through the numbers, you check your history book for the required matching value (running_prefix_sum - k), 
instantly add those past occurrences to your result, and then log your new current sum into the history 
book so it can help validate future subarrays down the line.
'''

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        encountered_sum = {0:1} # base case when we encounter sum k is there but we havent encountered 0
        
        running_prefix_sum = 0
        result = 0
        for num in nums:
            running_prefix_sum += num
            result += encountered_sum.get(running_prefix_sum-k, 0)
            encountered_sum[running_prefix_sum] = encountered_sum.get(running_prefix_sum, 0) + 1

        return result