'''
1774. Closest Dessert Cost
'''

'''
This solution finds the dessert cost closest to the target by exploring all combinations 
of base costs and toppings using a depth-first search (DFS). For each base cost, it 
recursively tries adding zero, one, or two of each topping to approach the target, 
updating the closest result whenever a closer or equally close but smaller cost is found. 
The recursion stops either when all toppings are considered or when the current cost 
exceeds the target, ensuring all feasible combinations are checked efficiently. Finally, 
the closest cost found across all base costs and topping combinations is returned.
'''

from typing import List


class Solution:
    def get_closest_with_base(self, curr_val, curr_ind, toppingCosts, target):
        if abs(target - curr_val) < abs(target - self.result) or \
           (abs(target - curr_val) == abs(target - self.result) and self.result > curr_val):
            self.result = curr_val

        if curr_ind == len(toppingCosts) or curr_val >= target:
            return
                
        self.get_closest_with_base(curr_val, curr_ind+1, toppingCosts, target)
        self.get_closest_with_base(curr_val + toppingCosts[curr_ind], curr_ind+1, toppingCosts, target)
        self.get_closest_with_base(curr_val + toppingCosts[curr_ind]*2, curr_ind+1, toppingCosts, target)

    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        self.result = 1_000_000
        for base in baseCosts:
            self.get_closest_with_base(base, 0, toppingCosts, target)
            
        return self.result
