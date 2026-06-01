'''
GFG - Longest Subarray with Sum K

Intuition: The intuition for this solution relies on a geographical tracking strategy where you use 
cumulative distances (prefix sums) to discover the longest possible stretch of road (subarray) that 
adds up exactly to k. Because any subarray sum is just the difference between your current running 
sum and a past running sum, finding a valid subarray means searching your history for a specific 
landmark value: prefix_sum - k. To maximize the length of this subarray, you want that starting 
landmark to be as far back in time as possible, which is why you use a hash map to lock in only 
the very first index where each unique running sum is born, refusing to overwrite it if that sum 
appears again later. By seeding the map with {0: -1} to gracefully catch valid subarrays that start 
all the way from the very first element, you can instantly calculate the maximum distance at each 
step by subtracting that earliest historic index from your current position, continuously updating 
your record for the longest valid subarray found.
'''

class Solution:
    def longestSubarray(self, arr, k):
        res = 0
        prefix_sum = 0
        prefix_sum_to_index_map = {0:-1}
        
        for i in range(len(arr)):
            prefix_sum += arr[i]
            if prefix_sum not in prefix_sum_to_index_map:
                prefix_sum_to_index_map[prefix_sum] = i
                
            required_num = prefix_sum - k
            if required_num in prefix_sum_to_index_map:
                res = max(res, i - prefix_sum_to_index_map[required_num])
        
        return res
