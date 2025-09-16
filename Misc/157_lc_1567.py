'''
1567. Maximum Length of Subarray With Positive Product
'''

'''
This solution finds the maximum length of a subarray with a positive 
product by iterating through the array while tracking the number of 
negative values encountered and the position of the first negative 
value within the current nonzero subarray. It resets the tracking 
variables when encountering zero (since zero breaks the subarray). 
If the count of negative numbers is even, the entire subarray from 
the start index contributes to the positive product length; if odd, 
the longest positive product subarray can exclude either the prefix 
up to the first negative number or the suffix after the last negative 
number. The result is updated at each step by computing these lengths, 
ensuring the maximum length of a positive product subarray is found 
efficiently in one pass with O(n) time complexity.
'''

class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        neg_val_count = 0
        n = len(nums)
        start = 0

        first_neg_ind = n
        res = 0

        for i in range(n):
            if nums[i] == 0:
                start = i+1
                first_neg_ind = n
                neg_val_count = 0
                continue
            
            if nums[i] < 0:
                first_neg_ind = min(first_neg_ind, i)
                neg_val_count += 1
            
            if neg_val_count % 2:
                res = max(res, i-first_neg_ind, first_neg_ind-start)
            else:
                res = max(res, i-start+1)
        
        return res