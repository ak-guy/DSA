class Solution:
    def getPossibility(self, array, min_distance, k, n):
        rem_cows = k-1
        last = array[0]
        
        for i in range(1, n):
            # we will put cow at index i, only if it is at certain minimum distance
            if array[i] - last >= min_distance:
                last = array[i]
                rem_cows -= 1
                
        return rem_cows <= 0
    
    def solve(self,n,k,stalls):
        stalls.sort()
        l = 1
        r = stalls[-1] - stalls[0]
        res = 0
        
        while l <= r:
            mid = (l + r) // 2 # we will try to find if we can acheive 'mid' as a maximum minimum distance
            cond = self.getPossibility(stalls, mid, k, n)
            if cond:
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid - 1
        
        return res