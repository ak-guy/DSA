from typing import List


class Solution:
    def __init__(self):
        self.mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.res = []

    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []

        def backtrack(recursion_depth, possible_res, n):
            if len(possible_res) == n:
                self.res.append("".join(possible_res.copy()))
                return

            for ind in range(len(self.mappings[digits[recursion_depth]])):
                possible_res.append(self.mappings[digits[recursion_depth]][ind])
                backtrack(recursion_depth + 1, possible_res, n)
                possible_res.pop()

        backtrack(0, [], n)
        return self.res
