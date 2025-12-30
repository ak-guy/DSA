"""
Fact 1 : Alex always goes first
Fact 2 : Number of piles (or length of piles) is even

Since alex is picking first, so he can pick either all even index or all odd index
it can be such that,
if alex picks all odd index, sum(piles[odd]) > sum(piles[even]) Alex wins
if alex picks all even index, sum(piles[odd]) < sum(piles[even]) Alex wins

so alex can go either way and win, hence alex will always win
"""

# # Method - 1 (Game Theory)
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True


# # Method - 2 (Recursion + Memoization)
class Solution:
    def stoneGame(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [[-1 for i in range(n)] for j in range(n)]

        def solve(l, r):
            if l > r:
                return 0
            if memo[l][r] != -1:
                return memo[l][r]

            p1L = nums[l] + min(
                solve(l + 2, r), solve(l + 1, r - 1)
            )  # considering p1 picks nums[l]
            p1R = nums[r] + min(
                solve(l, r - 2), solve(l + 1, r - 1)
            )  # considering p1 picks nums[r]

            max_score = max(p1L, p1R)
            memo[l][r] = max_score
            return memo[l][r]

        max_player_A_can_score = solve(0, n - 1)
        return max_player_A_can_score >= sum(nums) - max_player_A_can_score
