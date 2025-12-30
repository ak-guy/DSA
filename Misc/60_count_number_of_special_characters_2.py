from __future__ import annotations


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # -1 --> cannot change it later
        temp = [0 for i in range(26)]

        for char in word:
            is_lower = char.islower()

            if is_lower:
                if temp[ord(char) - 97] == 9:
                    temp[ord(char) - 97] = -1
                elif temp[ord(char) - 97] == 0:
                    temp[ord(char) - 97] = 10
            else:
                if temp[ord(char) - 65] == 0:
                    temp[ord(char) - 65] = -1
                elif temp[ord(char) - 65] == 10:
                    temp[ord(char) - 65] = 9

        res = 0
        for val in temp:
            if val == 9:
                res += 1
        return res


obj = Solution()
obj.numberOfSpecialChars("aaAbacBC")
