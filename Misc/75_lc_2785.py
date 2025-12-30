"""
2785. Sort Vowels in a String
"""


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = frozenset(["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"])

        vowels_in_s = []
        for char in s:
            if char in vowels:
                vowels_in_s.append(char)

        vowels_in_s.sort()

        res = ""
        i = 0
        for ind, char in enumerate(s):
            if char in vowels:
                res += vowels_in_s[i]
                i += 1
            else:
                res += char

        return res
