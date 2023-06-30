
'''
this solution wont work for leetcode as there we can have neg values also. One solution can be, we can use two
pointer approach on sorted arr
'''

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
