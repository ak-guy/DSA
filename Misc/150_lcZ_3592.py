'''
3592. Inverse Coin Change
'''

'''
The given solution reconstructs the coin denominations from a 
provided list numWays, where each element represents the number 
of ways to make change for amounts from 0 to n. It uses a dynamic 
programming approach to simulate the coin change counting process 
in reverse: starting with an initial DP array numWays_dp assuming 
no coins (only one way to make zero), it iterates through each 
index and compares the current DP count with the target numWays. 
If the DP count plus one matches the target at the next amount, 
it infers that a new coin of denomination i+1 was added, 
appends it to the results, and updates the DP array accordingly. 
If the counts match exactly without change, it moves forward, 
otherwise it returns an empty list indicating no valid coin 
combination exists. The final result is the list of coins that 
produce the given numWays array.
'''

class Solution:
    def findCoins(self, numWays: list[int]) -> list[int]:
        n = len(numWays)
        result = []
        numWays_dp = [0 for _ in range(n+1)]
        numWays_dp[0] = 1

        for i in range(n):
            if numWays_dp[i+1] + 1 == numWays[i]:
                result.append(i+1)
                for j in range(i+1, n+1):
                    numWays_dp[j] += numWays_dp[j-i-1]
            elif numWays_dp[i+1] == numWays[i]:
                continue
            else:
                return []
        
        return result
