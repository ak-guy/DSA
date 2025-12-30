"""
1910. Remove All Occurrences of a Substring
"""

from typing import List


# Using KMP algo
class Solution:
    def formLPSArray(self, pattern: str) -> List[int]:
        n = len(pattern)
        lps = [0 for i in range(n)]

        starting_index = 1
        prev_lps_value = lps[0]
        while starting_index < n:
            if pattern[starting_index] == pattern[prev_lps_value]:
                prev_lps_value += 1
                lps[starting_index] = prev_lps_value
                starting_index += 1
            else:
                if prev_lps_value == 0:
                    starting_index += 1
                else:
                    prev_lps_value = lps[prev_lps_value - 1]
        return lps

    def checkPaternInText(self, text: str, pattern: str):
        n = len(text)
        m = len(pattern)
        lps = self.formLPSArray(pattern)

        i = 0  # starting index of text
        j = 0  # starting index of pattern

        while i < n:
            if text[i] == pattern[j]:
                i += 1
                j += 1

            if j == m:  # found one solution
                return i - j
            elif i < n and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return None

    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)
        while True:
            starting_index = self.checkPaternInText(s, part)
            if starting_index is not None:
                s = s[:starting_index] + s[starting_index + n :]
            else:
                break

        return s
