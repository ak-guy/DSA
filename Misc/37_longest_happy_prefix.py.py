# # using kmp algo
from __future__ import annotations


class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        # longest prefix suffix, for an index i it will store max length of matching suffix and prefix till that index
        lps = [0 for i in range(n)]

        prev_lps_value, ind = 0, 1
        while (ind < n):
            if s[prev_lps_value] == s[ind]:
                lps[ind] = prev_lps_value + 1
                prev_lps_value += 1
                ind += 1
            else:
                if prev_lps_value == 0:
                    lps[ind] = 0
                    ind += 1
                else:
                    prev_lps_value = lps[prev_lps_value-1]
        # print(lps)
        return s[n-lps[-1]:]


'''
take example of 'acccbaaacccbaac'
its lps = [0,0,0,0,0,1,1,1,2,3,4,5,6,7,2]
'''
# obj = Solution()
# print(obj.longestPrefix(s='bobcat')) # [0, 0, 1, 0, 0, 0]
