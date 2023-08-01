# # GFG
class Solution:
    def countWays(self, N, S):
        mod = 10**3+3
        dp = [[[-1 for k in range(2)] for j in range(N)] for i in range(N)]
        def f(start, end, isTrue): # start, end, what_we_are_searching_for
            if start > end:
                return 0
                
            if start == end:
                if isTrue: # if we are searching for true then will return 1 if s[start] = 'T'
                    if S[start] == 'T': return 1
                    else: return 0
                else: # if we are searching for False then will return 1 if s[start] = 'F'
                    if S[start] == 'F': return 1
                    else: return 0
            
            if dp[start][end][isTrue] != -1:
                return dp[start][end][isTrue]
            
            res = 0
            for ind in range(start+1, end, 2):
                lt = f(start, ind-1, 1) # will return no of ways we can get True if we evaluate only S[start:ind]
                lf = f(start, ind-1, 0)
                rt = f(ind+1, end, 1)
                rf = f(ind+1, end, 0)
                
                if S[ind] == '|':
                    if isTrue:
                        res += ((((lt * rt) % mod) + ((lt * rf) % mod) + ((lf * rt) % mod)) % mod)
                    else:
                        res += ((lf * rf) % mod)
                        
                elif S[ind] == '&':
                    if isTrue:
                        res += ((lt * rt) % mod)
                    else:
                        res += ((((lf * rf) % mod) + ((lt * rf) % mod) + ((lf * rt) % mod)) % mod)
                        
                elif S[ind] == '^':
                    if isTrue:
                        res += ((((lt * rf) % mod) + ((lf * rt) % mod)) % mod)
                    else:
                        res += ((((lt * rt) % mod) + ((lf * rf) % mod)) % mod)
                        
            dp[start][end][isTrue] = res % mod
            
            return dp[start][end][isTrue]
        
        return f(0, N-1, 1) # we will check from 0th index to (N-1)th index how many ways we can get True(1 signifies that)