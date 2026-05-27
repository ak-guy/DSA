'''
974. Subarray Sums Divisible by K

Intuition: For the difference {prefixSum}[j] - {prefixSum}[i]) to be perfectly
divisible by k, both prefix sums must leave the exact same remainder when divided by k (i.e., 
{prefixSum}[i] % k == {prefixSum}[j] % k).The Optimized Approach (O(n)): Instead of storing 
actual sums or checking pairs, you maintain a running remainder (prefixMod) as you iterate 
through the array. You use a frequency array (modGroups) of size k to track how many times each 
remainder (0 to k-1) has appeared so far.Counting Valid Subarrays: Every time you encounter a 
remainder that you have seen before, it means a valid, divisible subarray has just been formed. 
You add the historical count of that remainder to your total answer, then increment its count by 
1 for future matches.

Handling the Edge Case: modGroups[0] is initialized to 1 at the very 
beginning. This ensures that if a running prefix sum is perfectly divisible by k all on its own 
(starting right from index 0), it is correctly counted as a valid subarray.
'''

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        # since we need to check whether we have encountered same modulus before, so
        # we know that it will range from 0 to k-1, so total k length of array is needed

        mod_encountered_count = [0 for _ in range(k)]

        # edge case: mod == 0, we will set the value as 1 because this will ensure if running
        # prefix sum is perfectly divisible by k. Ex - [3, 5]; k = 8
        mod_encountered_count[0] = 1

        running_prefix_sum = 0
        result = 0
        for num in nums:
            running_prefix_sum += num
            result += mod_encountered_count[running_prefix_sum % k]
            mod_encountered_count[running_prefix_sum % k] += 1

        return result
