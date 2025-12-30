"""
2420. Find All Good Indices
"""

"""
This code solves the problem of finding all "good indices" in an 
array where a good index is defined as an index such that the 
subarray of size k before it is non-increasing and the subarray 
of size k after it is non-decreasing. It does this by first 
computing two auxiliary arrays: prefix, where prefix[i] records 
the length of the longest non-increasing subarray ending at i, 
and postfix, where postfix[i] records the length of the longest 
non-decreasing subarray starting at i. Then, for each index ind 
from k to n-k-1, the code checks if the prefix value just before 
ind and the postfix value just after ind are both at least k. 
If so, ind is added to the result list, which is finally returned.
"""

from typing import List


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix = [1 for _ in range(n)]
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                prefix[i] = 1 + prefix[i - 1]

        postfix = [1 for _ in range(n)]
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                postfix[i] = 1 + postfix[i + 1]

        result = []
        for ind in range(k, n - k):
            if prefix[ind - 1] >= k and postfix[ind + 1] >= k:
                result.append(ind)

        return result
