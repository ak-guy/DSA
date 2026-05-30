'''
485. Max Consecutive Ones

Intuition: The intuition behind this solution relies on a dynamic window-expansion strategy 
where you dynamically measure the size of islands of ones as you discover them. The algorithm 
uses a main pointer (start) to scan the array until it hits a 1, marking the beginning of a 
consecutive streak, while ignoring zeroes along the way. Once a 1 is detected, a secondary 
scout pointer (end) is deployed right next to it to march forward and measure how far the 
streak extends, stopping only when it hits a 0 or the end of the array. The code then instantly 
calculates the length of this current streak by subtracting the two pointer positions (end - start), 
updates the global maximum (res) if this streak is the longest seen so far, and intelligently 
teleports the start pointer directly to the end position to immediately begin searching for the 
next island of ones without re-evaluating the territory already claimed.
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        start, end = 0, 0
        
        while start < n:
            if nums[start] != 1:
                start += 1
            else:
                end = start+1
                while end < n and nums[end] == 1:
                    end += 1
                res = max(res, end-start)
                start = end
        
        return res
