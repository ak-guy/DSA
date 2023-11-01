'''
Find how much maximum player A can score, then player will score => sum(nums) - max_player_A_can_score
'''

# # Method - 1 (Recursion)
from typing import List
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def solve(l,r):
            if l > r:
                return 0

            # we will take min() because after player 1 picks nums[l] or nums[r] player 2 will pick that value which results in minimizing the score of player 1
            p1L = nums[l] + min(solve(l+2,r), solve(l+1,r-1)) # considering p1 picks nums[l]
            p1R = nums[r] + min(solve(l,r-2), solve(l+1,r-1)) # considering p1 picks nums[r]

            max_score = max(p1L, p1R)
            return max_score
        
        max_player_A_can_score = solve(0, len(nums)-1)
        return max_player_A_can_score >= sum(nums) - max_player_A_can_score
    

# # Method - 2 (Recursion + Memoization)
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [[-1 for i in range(n)] for j in range(n)]
        
        def solve(l,r):
            if l > r:
                return 0
            if memo[l][r] != -1:
                return memo[l][r]

            p1L = nums[l] + min(solve(l+2,r), solve(l+1,r-1)) # considering p1 picks nums[l]
            p1R = nums[r] + min(solve(l,r-2), solve(l+1,r-1)) # considering p1 picks nums[r]

            max_score = max(p1L, p1R)
            memo[l][r] = max_score
            return memo[l][r]
        
        max_player_A_can_score = solve(0, n-1)
        return max_player_A_can_score >= sum(nums) - max_player_A_can_score