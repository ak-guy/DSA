# this method might give TLE because suppose we need to find (10th root of 10^9) then mid = 5*(10^8) now
# calculating it power mid ^ 10 will be unnecesary and will give TLE
class Solution:
    # calculating A^B using binary exponentiation which have TC -> O(log(b))
    def calculate_A_raiseto_B(self, a, b):
        res = 1
        while b>0:
            if b%2:
                res *= a
            a *= a
            b >>= 1
        
        return res
    
    def NthRoot(self, n, m):
        l = 1
        r = m
        while l <= r:
            mid = (l+r) // 2
            val = self.calculate_A_raiseto_B(mid, n)
            if val == m:
                return mid
            elif val > m:
                r = mid-1
            else:
                l = mid+1
        return -1
    
# # optimizing by not calculating unnecessary powers
class Solution:
    # calculating A^B using binary exponentiation which have TC -> O(log(b))
    def calculate_A_raiseto_B(self, a, b, m):
        res = 1
        while b>0:
            if b%2:
                res *= a
            if res > m: # if at point while calculating we found result to be bigger than what we are expecting, we return 0
                return 0
            a *= a
            b >>= 1
        
        if res == m:
            return 1
        else:
            return 2
    
    def NthRoot(self, n, m):
        l = 1
        r = m
        while l <= r:
            mid = (l+r) // 2
            val = self.calculate_A_raiseto_B(mid, n, m)
            if val == 1:
                return mid
            elif val == 0:
                r = mid-1
            else:
                l = mid+1
        return -1