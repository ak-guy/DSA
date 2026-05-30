'''
136. Single Number

Intuition: The intuition behind this incredibly efficient solution lies in the magical mathematical 
properties of the bitwise XOR (∧) operation, which essentially acts as a toggle switch that perfectly 
cancels out duplicates. XOR has two rules that make it perfect for this problem: any number XORed with 
itself becomes zero (A∧A=0), and any number XORed with zero stays exactly the same (A∧0=A). Because the 
order in which you perform XOR operations doesn't matter, running a cumulative XOR across the entire 
array acts like a self-cleaning filter: every pair of identical numbers will inevitably find each other 
and cancel each other out into complete nothingness (zero), regardless of where they are standing in 
line. As a result, when the loop finishes crunching through the numbers, all the duplicates have 
successfully vanished, leaving the lone, unpaired single number as the sole survivor stored inside res.
'''

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        return res
