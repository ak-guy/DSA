'''
523. Continuous Subarray Sum

Intuition: The intuition for this solution blends the remainder-matching trick from "Subarray Sums Divisible by K" 
with a strict tracking mechanism to enforce the problem's constraint that the subarray must be at least two elements 
long. Mathematically, a contiguous subarray is a multiple of k if its sum leaves a remainder of 0 when divided by 
k. Because any subarray sum is just the difference between two prefix sums, a valid subarray exists if our current 
running remainder (running_sum_mod) matches a remainder we have already seen and stored in our history book (mod_dict).
However, to ensure this matching remainder wasn't just created by the single, current number you just added, the code 
uses a prev_mod_val variable to remember the exact remainder from the very last step. If your current remainder matches 
a historical one, it is guaranteed to span at least two elements as long as it isn't identical to the immediately 
preceding step's remainder (running_sum_mod != prev_mod_val). In the rare edge case where the current remainder is the 
same as the previous one, it means the current number itself was a multiple of k (a single-element subarray); the 
code safely bypasses this unless that remainder has appeared even earlier in history (mod_dict[running_sum_mod] > 1), 
which would confidently rescue the "at least two elements" rule.
'''

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        mod_dict = {0:1}

        prev_mod_val = 0
        running_sum = 0
        for num in nums:
            running_sum += num
            running_sum_mod = running_sum % k
            if running_sum_mod in mod_dict and (running_sum_mod != prev_mod_val or mod_dict[running_sum_mod] > 1):
                return True
            prev_mod_val = running_sum_mod
            mod_dict[running_sum_mod] = mod_dict.get(running_sum_mod, 0) + 1

        return False
