'''
Fact 1 : Alex always goes first
Fact 2 : Number of piles (or length of piles) is even

Since alex is picking first, so he can pick either all even index or all odd index
it can be such that, 
if alex picks all odd index, sum(piles[odd]) > sum(piles[even]) Alex wins
if alex picks all even index, sum(piles[odd]) < sum(piles[even]) Alex wins

so alex can go either way and win, hence alex will always win
'''
from typing import List
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True