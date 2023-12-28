# # Brute Force (Gives TLE)
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            if i==0 or (i>0 and nums[i-1] != 1):
                start = i
                temp_res = 0
                temp_k = k
                while start < n:
                    if nums[start] == 1:
                        temp_res += 1
                    elif nums[start] == 0 and temp_k:
                        temp_res += 1
                        temp_k -= 1
                    else:
                        break
                    start += 1
                res = max(res, temp_res)
        
        return res
    

# # Optimized Approach
