"""
3290. Maximum Multiplication Score
"""

from typing import List


# Method 1 - Recursion + Memoization
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        a_len = 4
        b_len = len(b)
        res = 0
        dp = [[-1 for _ in range(b_len)] for _ in range(4)]

        def helper(a_ind, b_ind):
            nonlocal res
            if a_ind >= a_len or b_ind >= b_len:
                return 0

            if dp[a_ind][b_ind] != -1:
                return dp[a_ind][b_ind]

            # pick case
            pick = helper(a_ind + 1, b_ind + 1) + a[a_ind] * b[b_ind]

            # not_pick case
            not_pick = -1_000_000_000_000_007
            if b_len - b_ind > a_len - a_ind:
                not_pick = helper(a_ind, b_ind + 1)

            res = max(pick, not_pick)
            dp[a_ind][b_ind] = res
            return res

        helper(0, 0)
        return res


# Method 2 - DP
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        a_len = 4
        b_len = len(b)
        res = -1_000_000_000_007
        dp = [[0 for _ in range(b_len + 1)] for _ in range(5)]

        for a_ind in range(3, -1, -1):
            for b_ind in range(b_len - 1, -1, -1):
                pick = dp[a_ind + 1][b_ind + 1] + (a[a_ind] * b[b_ind])

                not_pick = -1_000_000_000_000_007
                if b_len - b_ind > a_len - a_ind:
                    not_pick = dp[a_ind][b_ind + 1]

                res = max(pick, not_pick)
                dp[a_ind][b_ind] = res

        return dp[0][0]
