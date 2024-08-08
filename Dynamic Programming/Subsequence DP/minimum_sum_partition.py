
'''
this solution wont work for leetcode as there we can have neg values also. One solution can be, we can use two
pointer approach on sorted arr
'''
# Method 1 : DP (MeMoization)
from typing import List
class Solution:
    def mem_dp(self, ind: int, target: int, arr: List[int], dp: List[List[int]]) -> bool:
        if target == 0:
            return True
            
        if ind == 0:
            return arr[ind] == target
        
        if dp[ind][target] != -1:
            return dp[ind][target]
        
        not_pick = self.mem_dp(ind-1, target, arr, dp)

        pick = False
        if target >= arr[ind]:
            pick = self.mem_dp(ind-1, target-arr[ind], arr, dp)
        
        dp[ind][target] = pick or not_pick
        return dp[ind][target]

    def solve(self, arr):
        n = len(arr)
        total_sum = sum(arr)
        print(total_sum)
        dp = [[-1 for _ in range(total_sum+1)] for _ in range(n)]

        for possible_target in range(1, total_sum + 1):
            self.mem_dp(n-1, possible_target, arr, dp)
        
        res = 1_000_000_000
        for possible_sum in range(total_sum+1):
            if dp[n-1][possible_sum]:
                diff_bw_two_subsequence = abs(possible_sum - (total_sum-possible_sum))
                res = min(res, diff_bw_two_subsequence)
                
        return res


# Method 2 : DP (Tabulation)
class Solution:
    def minDifference(self, arr, n):
        summ = sum(arr)
        
        dp = [[False for i in range(summ+1)] for j in range(n)]
        
        for i in range(n):
            dp[i][0] = True
            
        # second base case done
        if arr[0] <= summ:
            dp[0][arr[0]] = True
        
        for i in range(1,n):
            for s in range(summ, -1, -1):
                not_pick = dp[i-1][s]
                
                pick = False
                if s>=arr[i]:
                    pick = dp[i-1][s-arr[i]]
                
                dp[i][s] = pick or not_pick    
        
        # # print(dp[n-1]) # this row tells us what all sum is possible 
        
        res = 10**5
        for i in range(summ):
            if dp[n-1][i] == True:
                res = min(res, abs(summ - i - i))
        
        return res
