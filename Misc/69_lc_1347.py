"""
1347. Minimum Number of Steps to Make Two Strings Anagram
"""

from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = Counter(s)
        counter_t = Counter(t)

        res = 0
        for s_key in counter_s.keys():
            s_key_count = counter_s[s_key]
            s_key_count_in_t = counter_t.get(s_key, 0)
            if s_key_count >= s_key_count_in_t:
                res += s_key_count - s_key_count_in_t

        return res
