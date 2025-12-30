class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        st = []
        count = 0
        for char in s:
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
            res = max(res, count)

        return res
