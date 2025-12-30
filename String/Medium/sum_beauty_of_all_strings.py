# using array
class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            char_count = [0 for k in range(26)]
            for j in range(i, n):
                char_count[ord(s[j]) - 97] += 1
                least = 1000
                most = max(char_count)
                for k in range(26):
                    if char_count[k] == 0:
                        continue
                    else:
                        least = min(least, char_count[k])
                res += most - least

        return res


# Using dictionary
class Solution:
    def beautySum(self, s):
        n = len(s)
        res = 0
        for i in range(n):
            char_count = {}
            for j in range(i, n):
                char_count[s[j]] = 1 + char_count.get(s[j], 0)
                res += max(char_count.values()) - min(char_count.values())
        return res
