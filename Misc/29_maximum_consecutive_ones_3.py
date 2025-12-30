# # Brute Force (Gives TLE)
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            if i == 0 or (i > 0 and nums[i - 1] != 1):
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
class Solution:
    """
    Algo : we will maintain a window of some size if k >= 0, otherwise shrink the window size by 1
    """

    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        for end in range(len(nums)):
            # if we encounter 0 then decrease k
            if nums[end] == 0:
                k -= 1

            # if we dont have enough k
            if k < 0:
                # if our nums[start] becomes zero then we inc our k count because we will be start too by 1 so this nums[start] will fall out of current window
                if nums[start] == 0:
                    k += 1

                # shrink the window
                start += 1

        return end - start + 1
