from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # first iteration, handling -ve integers
        for ind in range(n):
            if nums[ind] < 0:
                nums[ind] = 0
            
        # second iteration, marking nums[ind] as -ve if satifies few condition
        for ind in range(n):
            if abs(nums[ind]) > n or nums[ind] == 0:
                continue
            elif abs(nums[abs(nums[ind]) - 1]) == 0: # edge case where we have to mark the value present at ind (abs(nums[ind])) - 1 is equal to 0
                nums[abs(nums[ind]) - 1] = -1 * (n+1)
            else:
                nums[abs(nums[ind]) - 1] = -1 * abs(nums[abs(nums[ind]) - 1])
        
        # print(nums) # for debugging

        # third iteration, 
        for ind in range(n):
            if nums[ind] >= 0:
                return ind+1

        return n+1
    