'''
search space will be 1 till x
can apply BS and check if arr[mid] * arr[mid] <= x or not
'''
class Solution:
    def floorSqrt(self, x):
        if x == 0:
            return 0
        l = 1
        r = x
        ans = 1
        while l <= r:
            m = (l+r) // 2
            if (m*m) <= x:
                ans = m
                l = m+1
            else:
                r = m-1
        
        return ans # can return either ans or r