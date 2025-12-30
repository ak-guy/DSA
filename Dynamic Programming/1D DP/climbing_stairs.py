# # Method - 1 (Brute Force)(Recursion)
class Solution:
    # Function to count number of ways to reach the nth stair.
    def countWays(self, n):
        mod = 10**9 + 7

        def solve(i):
            if i == n:
                return 1
            if i > n:
                return 0

            step1 = solve(i + 1)
            step2 = solve(i + 2)

            return (step1 + step2) % mod

        val = solve(0) % mod
        return val


# # Method - 2 (Recursion + Memoization)(bottom up)
class Solution:
    # Function to count number of ways to reach the nth stair.
    def countWays(self, n):
        mod = 10**9 + 7
        dp = [-1] * n

        def solve(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if dp[i] != -1:
                return dp[i]

            step1 = solve(i + 1)
            step2 = solve(i + 2)

            dp[i] = (step1 + step2) % mod

            return dp[i]

        val = solve(0) % mod
        return val


# # Method - 3 (Tabulation)(bottom up)
class Solution:
    # Function to count number of ways to reach the nth stair.
    def countWays(self, n):
        mod = 10**9 + 7
        dp = [-1] * n
        dp[0] = 1
        if n > 1:
            dp[1] = 2

        if n == 1 or n == 2:
            return dp[n - 1]

        for i in range(2, n):
            dp[i] = (dp[i - 1] + dp[i - 2]) % mod

        val = dp[n - 1] % mod
        return val


# # Method - 4 (Tabulation)(Space Optimization)
class Solution:
    # Function to count number of ways to reach the nth stair.
    def countWays(self, n):
        mod = 10**9 + 7
        prev = 1
        curr = 2
        if n == 1 or n == 2:
            return n

        for i in range(2, n):
            temp = curr
            curr = (curr + prev) % mod
            prev = temp % mod

        return curr
