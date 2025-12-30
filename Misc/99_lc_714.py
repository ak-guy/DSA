"""
714. Best Time to Buy and Sell Stock with Transaction Fee
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:  # memoization
        n = len(prices)
        dp = [[-1 for _ in range(2)] for _ in range(n + 1)]

        def helper(ind, isBought):
            if ind == n:
                return 0
            if dp[ind][isBought] != -1:
                return dp[ind][isBought]

            profit = 0
            if not isBought:
                profit = max(
                    helper(ind + 1, False), helper(ind + 1, True) - prices[ind]
                )
            else:
                profit = max(
                    helper(ind + 1, True), helper(ind + 1, False) + (prices[ind] - fee)
                )

            dp[ind][isBought] = profit
            return dp[ind][isBought]

        helper(0, False)
        return dp[0][0]

    def maxProfit2(self, prices: List[int], fee: int):  # tablulation
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n + 1)]

        for ind in range(n - 1, -1, -1):
            for buySell in range(2):
                profit = 0
                if buySell == 0:
                    profit = max(dp[ind + 1][0], dp[ind + 1][1] - prices[ind])
                else:
                    profit = max(dp[ind + 1][1], dp[ind + 1][0] + prices[ind] - fee)
                dp[ind][buySell] = profit

        return dp[0][0]
