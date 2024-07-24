'''
2161. Partition Array According to Given Pivot
'''

from typing import List
# Method 1 : using filter function
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = list(filter(lambda x: x < pivot, nums))
        pivot_values = list(filter(lambda x: x == pivot, nums))
        right = list(filter(lambda x: x > pivot, nums))

        return left + pivot_values + right
    
# Method 2 : Using custom sort
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        nums.sort(key=lambda x:-1 if x<pivot else (0 if x==pivot else 1))
        return nums