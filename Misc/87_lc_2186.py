'''
2186. Minimum Number of Steps to Make Two Strings Anagram II
'''

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_mappings = {}
        for ind in range(len(s)):
            s_mappings[s[ind]] = 1 + s_mappings.get(s[ind], 0)
        
        t_mappings = {}
        for ind in range(len(t)):
            t_mappings[t[ind]] = 1 + t_mappings.get(t[ind], 0)
        
        res = 0
        for ind in range(26):
            s_count = s_mappings.get(chr(ind+97), 0)
            t_count = t_mappings.get(chr(ind+97), 0)
            if s_count != t_count:
                res += abs(s_count - t_count)

        return res
