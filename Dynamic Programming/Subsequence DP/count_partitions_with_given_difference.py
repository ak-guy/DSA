'''
same as count subset with summ k, only difference is target summ, here

s1 - s2 = d
but, s1 + s2 = total ====> s1 = total - s2
total - s2 - s2 = d =====> s2 = ( total - d ) // 2
also ( total - d ) must be even
'''
# # Method - 1 (Recursion + Memoization)
# class Solution:
#     def countPartitions(self, n, d, arr):
#         mod = 10**9 + 7
#         def f(i, total, dp):
#             if i == 0:
#                 if total == 0 and arr[0] == 0:
#                     return 2
#                 elif total == 0 or total == arr[0]:
#                     return 1
#                 else:
#                     return 0
                
#             if dp[i][total] != 0:
#                 return dp[i][total]
            
#             not_pick = f(i-1, total, dp)
#             pick = 0
#             if total>=arr[i]:
#                 pick = f(i-1, total-arr[i], dp)
            
#             dp[i][total] = (pick + not_pick) % mod
            
#             return dp[i][total]
        
#         total = sum(arr)
        
#         if (total-d) % 2:
#             return 0
#         target = (total-d) // 2

#         dp = [[0 for i in range(target+1)] for j in range(n)]
        
#         return f(n-1, target, dp)

# # Method - 2 (DP)
# class Solution:
#     def countPartitions(self, n, d, arr):
#         mod = 10**9 + 7
#         total = sum(arr)
        
#         if total - d < 0:
#             return 0
        
#         if (total-d) % 2:
#             return 0
            
#         target = (total-d) // 2
#         dp = [[0 for i in range(target+1)] for j in range(n)]
        
#         dp[0][0] = 1
        
#         if target >= arr[0]:
#             dp[0][arr[0]] = 1
        
#         if arr[0] == 0:
#             dp[0][0] = 2
            
#         for i in range(1, n):
#             for j in range(target+1):
#                 not_pick = dp[i-1][j]

#                 pick = 0
#                 if j>=arr[i]:
#                     pick = dp[i-1][j-arr[i]]
                
#                 dp[i][j] = (not_pick + pick) % mod
        
#         return dp[n-1][target]

# # Method - 3 (Space Optimization)
class Solution:
    def countPartitions(self, n, d, arr):
        mod = 10**9 + 7
        total = sum(arr)
        
        if total - d < 0:
            return 0
        
        if (total-d) % 2:
            return 0
            
        target = (total-d) // 2
        prev = [0 for i in range(target+1)]

        prev[0] = 1
        
        if target >= arr[0]:
            prev[arr[0]] = 1
        
        if arr[0] == 0:
            prev[0] = 2
            
        for i in range(1, n):
            curr = [0 for k in range(target+1)]
            for j in range(target+1):
                not_pick = prev[j]

                pick = 0
                if j>=arr[i]:
                    pick = prev[j-arr[i]]
                
                curr[j] = (not_pick + pick) % mod
            prev = curr
        
        return prev[target]
    
obj = Solution()
var = obj.countPartitions(4, 0, [1, 1, 1, 1])
print(var)