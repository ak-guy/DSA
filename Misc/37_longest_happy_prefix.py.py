# # using kmp algo
from __future__ import annotations


class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0 for i in range(n)]  # longest  prefix suffix

        prev_lps_value, ind = 0, 1
        while (ind < n):
            if s[prev_lps_value] == s[ind]:
                lps[ind] = prev_lps_value + 1
                prev_lps_value += 1
                ind += 1
            else:
                if prev_lps_value == 0:
                    ind += 1
                else:
                    prev_lps_value = lps[prev_lps_value-1]
        print(lps)
        return s[n-lps[-1]:]


obj = Solution()
obj.longestPrefix(s='ababab')
