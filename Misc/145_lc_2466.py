'''
2466. Count Ways To Build Good Strings
'''

# # Method - 1 (Recursion)
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        def rec(end):
            if end == 0:
                return 1
            
            count = 0
            if end >= zero:
                count += rec(end-zero)
            if end >= one:
                count += rec(end-one)
            
            return count % 1_000_000_007
        
        res = 0
        for val in range(low, high+1):
            res += rec(val) % 1_000_000_007
        
        return res % 1_000_000_007
    
# # Method - 2 (Memoization)
'''
The solution uses a top-down dynamic programming approach with memoization 
to count the number of good strings whose lengths lie between low and high. 
It recursively computes the number of ways to build strings of a given length 
by appending blocks of zeros (length zero) or ones (length one) until the 
desired length is achieved. Results are cached in a dp array to avoid redundant 
calculations, and all counts are taken modulo 109+7109+7. Finally, it sums the 
counts for all lengths between low and high to return the total number of good 
strings efficiently.
'''
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 1_000_000_007
        dp = [-1 for _ in range(high+1)]

        def rec(end):
            if end == 0:
                return 1
            if dp[end] != -1:
                return dp[end]
            
            count = 0
            if end >= zero:
                count += rec(end-zero)
            if end >= one:
                count += rec(end-one)
            dp[end] = count % mod
            return dp[end]
        
        res = 0
        for val in range(low, high+1):
            res += rec(val) % mod
        
        return res % mod
