# Same logic as Frog Jump 1

# # Method - 1 (Recursion + Memoization)
from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [-1 for i in range(n)]
        def f(i):
            if i == 0:
                return min(costs)
            if dp[i] != -1:
                return dp[i]

            day_number = days[i]
            day_less_7 = day_number - 7
            day_less_30 = day_number - 30

            day_7 = -1
            for j in range(i, -1, -1):
                if days[j] <= day_less_7:
                    day_7 = j
                    break
            
            day_30 = -1
            for j in range(i, -1, -1):
                if days[j] <= day_less_30:
                    day_30 = j
                    break
            
            step_1 = f(i-1) + costs[0]
            step_2 = costs[1]
            if day_7>=0:
                step_2 = f(day_7) + costs[1]

            step_3 = costs[2]
            if day_30>=0:
                step_3 = f(day_30) + costs[2]

            dp[i] = min(step_1, step_2, step_3)
            return dp[i]

        return f(n-1)
    

# # Method - 2 (Tabulation)
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0 for i in range(n)]
        dp[0] = min(costs)
        res = 1e5
        for i in range(1,n):
            day_number = days[i]
            day_less_7 = day_number - 7
            day_less_30 = day_number - 30

            day_7 = -1
            for j in range(i, -1, -1):
                if days[j] <= day_less_7:
                    day_7 = j
                    break
            
            day_30 = -1
            for j in range(i, -1, -1):
                if days[j] <= day_less_30:
                    day_30 = j
                    break
            
            step_1 = dp[i-1] + costs[0]
            step_2 = costs[1]
            if day_7>=0:
                step_2 = dp[day_7] + costs[1]

            step_3 = costs[2]
            if day_30>=0:
                step_3 = dp[day_30] + costs[2]
            
            dp[i] = min(res, step_1, step_2, step_3)
        return dp[n-1]