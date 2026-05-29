'''
268. Missing Number

Intuition: The intuition behind this solution is a variation of the Index as a Hash Map pattern, 
where the array itself is cleverly used to record the presence of numbers by turning the values 
at corresponding indices negative. Since an array of length n expects a complete set of numbers 
from 0 to n, the code appends a dummy element to prevent out-of-bounds errors, and then iterates 
through the list treating the absolute value of each number as an index destination. When a number 
is processed, the code visits that number's corresponding index and flags it as "seen" by 
multiplying its value by -1, while utilizing specific mathematical workarounds like -INT_MAX to 
separately track the tricky edge cases involving the number 0 (which cannot be made negative) and 
existing negative placeholders. Finally, the algorithm scans the modified array from left to right; 
the very first index that still contains a positive, unflagged number reveals the exact missing value 
in the sequence, as no number in the input ever pointed to that slot to turn it negative.
'''

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        INT_MAX = 10000000007
        n = len(nums)
        nums.append(n+1)

        for i in range(n):
            if nums[i] != -INT_MAX and nums[abs(nums[i])] == 0:
                nums[abs(nums[i])] = -1 * INT_MAX
            elif nums[i] == -INT_MAX:
                nums[0] *= -1
            else:
                nums[abs(nums[i])] = -1 * nums[abs(nums[i])]

        for i in range(n+1):
            if nums[i] >= 0:
                return i
