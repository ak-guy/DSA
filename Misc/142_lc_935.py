"""
935. Knight Dialer
"""


# Method 1 - Recursion
class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 1_000_000_007
        mapping = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6],
        }

        cache = {}

        def f(num, step):
            """
            params:
                num -> position on dialer at which we are currently present
                step -> number of time we can move knight
            return:
                type -> int
                value -> will return how many distinct phone numbers can be created with length step+1 and
                         ending with num
            """
            if (num, step) in cache:
                return cache[(num, step)]

            if step == 0:
                return 1

            ans = 0
            for to_reach in mapping[num]:
                ans += f(to_reach, step - 1)
                cache[(num, step)] = ans
            return ans

        res = 0
        for i in range(10):
            res += f(i, n - 1) % mod
        return res % mod


# Method 2 - DP with Space Optimization
class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 1_000_000_007
        mapping = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6],
        }

        dp = [1 for _ in range(10)]  # for step 0

        for nth_jump in range(n - 1):
            next_jump_dp = [0 for _ in range(10)]
            for num in range(10):
                for to_reach in mapping[num]:
                    next_jump_dp[num] += dp[to_reach]

            dp = next_jump_dp

        return sum(dp) % mod

    """
    0 = dp[4] + dp[6]
    1 = dp[6] + dp[8]
    .
    .
    .
    and so on
    
      jumps 
            0   1   2   3   4   5   6   7   8   9
        0   1   1   1   1   1   1   1   1   1   1   -> dp
        1   2   2   2   2   3   0   3   2   2   2   -> next_jump_dp
        2   6   5   4   5   6   0   6   5   4   5
        -
        -
        -
        -
    """
