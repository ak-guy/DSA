'''
2944. Minimum Number of Coins for Fruits
'''

'''
This solution uses a top-down dynamic programming approach with 
memoization to find the minimum number of coins needed to acquire 
all fruits given a special offer: buying the i-th fruit allows free 
acquisition of the next i fruits. The recursive helper function 
helper(i) calculates the minimum cost starting from the i-th fruit 
by trying all possible next purchase positions within the range 
from i+1 to 2*(i+1) (since buying fruit at i allows getting up to 
the next i fruits for free). It adds the price of the current fruit 
to the minimum cost returned for those future states, and memoizes 
results in the dp array to avoid recomputation. The function returns 
the cost of buying the fruit at position 0 plus the minimum cost of 
subsequent purchases, ensuring an optimal strategy. This approach 
efficiently explores all buying options while leveraging the free 
fruit offer to minimize total coins spent.
'''


class Solution:
    def minimumCoins(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [-1 for _ in range(n)]

        def helper(i):
            if i >= n: return 0
            if dp[i] != -1: return dp[i]

            min_coins = 1_000_000_007
            for next_jump in range(i+1, min(n, 2*(i+1)) + 1):
                min_coins = min(min_coins, helper(next_jump))

            dp[i] = prices[i]+min_coins
            return dp[i]
        
        return helper(0)
