'''
search space will be 1 to max(piles), then we will apply BS and check if koko
can finish that within h hours
'''
import math
class Solution:
    def Solve(self, N, piles, h): # O(nlog(max(piles)))
        l = 1
        r = res = max(piles)
        n = len(piles)

        while l <= r:
            mid = (l+r) // 2

            hours = 0
            for i in range(n):
                hours += math.ceil(piles[i] / mid)
            if hours <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res