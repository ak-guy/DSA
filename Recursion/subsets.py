# print all subsets, all numbers are unique
from typing import List

class Solution:
    def __init__(self):
        self.res = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def recursion(recursion_depth, subset):
            # print(f'recursion_depth = {recursion_depth}, and subset = {subset}')
            nonlocal n
            if recursion_depth == n:
                self.res.append(subset.copy())
                return
            
            subset.append(nums[recursion_depth])
            recursion(recursion_depth + 1, subset)
            
            subset.pop()
            recursion(recursion_depth + 1, subset)

        recursion(0, [])
        return self.res
    
# obj = Solution()
# obj.subsets(nums=[1,2,3])