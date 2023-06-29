# # Same as subset_sum, just difference is, here target_summ will be half sum of array elements

class Solution:
    def equalPartition(self, N, arr):
        target_sum = sum(arr)
        if target_sum % 2:
            return 0
        else:
            target_sum /= 2
        
        target_sum = int(target_sum)
        
        dp = [[-1 for i in range(target_sum+1)] for j in range(N)]
        def f(i, total):
            if total == 0:
                return True
                
            if i == 0:
                return total == arr[0] # we will consider only pick in this case because in previous not_pick is handled
            
            if dp[i][total] != -1:
                return dp[i][total]
            
            not_pick = f(i-1, total)
            
            pick = False
            if total >= arr[i]:
                pick = f(i-1, total - arr[i])
            
            dp[i][total] = pick or not_pick
            
            return dp[i][total]
            
        return f(N-1, target_sum)