# # Method - 1 (Recursion)
class Solution:
    def maximumPoints(self, a, n):
        # res = 0
        def f(r, lp):
            # row, last_picked
            if r == 0:
                maxi = 0
                for i in range(3):
                    if i != lp:
                        maxi = max(maxi, a[0][i])
                return maxi
            
            maxi = 0
            for i in range(3):
                if i != lp:
                    val = f(r-1, i) + a[r][i]
                    maxi = max(maxi, val)
                    
            return maxi
            
        return f(n-1, 3)
    
# # Method - 2 (Recursion + Memoization)
class Solution:
    def maximumPoints(self, a, n):
        dp = [[-1 for j in range(4)] for i in range(n)]
        # dp = [[-1]*4]*n
        '''dp = [[-1]*4]*n -> we can use this but it will cause unexpected behavior
            In this method, each row will be referencing the same column. This means,
            even if we update only one element of the array, it will update same column 
            in our array.
        '''
        def f(r, lp):
            # row, last_picked
            if dp[r][lp] != -1:
                # print("already solved" + str(dp[r][lp]))
                return dp[r][lp]
                
            if r == 0:
                maxi = 0
                for i in range(3):
                    if i != lp:
                        maxi = max(maxi, a[0][i])
                dp[r][lp] = maxi
                # print("max of last row" + str(dp[r][lp]))
                return dp[r][lp]
                
            maxi = 0
            for i in range(3):
                if i != lp:
                    val = f(r-1, i) + a[r][i]
                    maxi = max(maxi, val)
                    
            dp[r][lp] = maxi
            # print("return value" + str(dp[r][lp]))
            return dp[r][lp]
            
        return f(n-1, 3)
    
# # Method - 3 (DP)(Tabulation)
class Solution:
    def maximumPoints(self, a, n):
        dp = [[-1 for j in range(4)] for i in range(n)]

        # base case
        dp[0][0] = max(a[0][1], a[0][2])
        dp[0][1] = max(a[0][0], a[0][2])
        dp[0][2] = max(a[0][0], a[0][1])
        dp[0][3] = max(a[0][0], a[0][1], a[0][2])
        
        for r in range(1, n):
            for lp in range(4):
                maxi = 0
                for i in range(3):
                    if i != lp:
                        val = dp[r-1][i] + a[r][i]
                        maxi = max(maxi, val)
                        
                dp[r][lp] = maxi
        
        return dp[n-1][3]
    
# # Method - 4 (Space Optimization)
class Solution:
    def maximumPoints(self, a, n):
        prev = [0 for i in range(4)]
        
        prev[0] = max(a[0][1], a[0][2])
        prev[1] = max(a[0][0], a[0][2])
        prev[2] = max(a[0][0], a[0][1])
        prev[3] = max(a[0][0], a[0][1], a[0][2])
        
        for r in range(1, n):
            curr = [0 for i in range(4)]
            for lp in range(4):
                maxi = 0
                for i in range(3):
                    if i != lp:
                        val = prev[i] + a[r][i]
                        maxi = max(maxi, val)
                        
                curr[lp] = maxi
            
            prev = curr
        
        return prev[3]
