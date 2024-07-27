'''
2317. Maximum XOR After Operations
'''

from typing import List
class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        bits = [0 for i in range(36)]
        for num in nums:
            nth_bit = 0
            while num:
                if num % 2:
                    bits[nth_bit] = 1
                nth_bit += 1
                num >>= 1

        res = 0
        for ind, bit in enumerate(bits):
            if bit:
                res += (1 << ind)
        
        return res
    
# Method 2 : we can get result by simply taking or of all element
class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res |= num
        
        return res