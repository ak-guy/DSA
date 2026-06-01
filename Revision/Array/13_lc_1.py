'''
1. Two Sum

Intuition: The intuition behind this solution relies on turning a blind search for two matching 
numbers into a proactive memory-lookup strategy using a hash map. Instead of wasting time 
checking every possible pair of numbers in the array, you iterate through the list step-by-step 
and calculate the exact missing piece (needed = target - nums[i]) that your current number 
equires to successfully hit the target. You then immediately consult your "memory book" 
(num_to_ind_map) to see if you have already encountered that exact missing piece earlier in your 
journey. If it is already in the map, a perfect match has been found, and you can instantly return 
the current index along with the stored historic index; if it isn't there yet, you simply log your 
current number and its index into the map so that future numbers moving down the line can look back 
and claim it as their missing piece.
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_ind_map = {}
        
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in num_to_ind_map:
                return [i, num_to_ind_map[needed]]
            
            num_to_ind_map[nums[i]] = i
    