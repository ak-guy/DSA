from typing import List

class Solution:
    def __init__(self):
        self.res = []

    def partition(self, s: str) -> List[List[str]]:
        def backtrack(recursion_depth, possible_res, n):
            print(f'recursion_depth = {recursion_depth} and possible_res = {possible_res}')
            if recursion_depth == n:
                self.res.append(possible_res.copy())
                return

            for ind in range(recursion_depth, n):
                if self.isPalindrome(recursion_depth, ind, s):
                    possible_res.append(s[recursion_depth:ind+1])
                    backtrack(ind + 1, possible_res, n)
                    possible_res.pop()

        backtrack(0, [], len(s))
        return self.res

    def isPalindrome(self, l, r, s):
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

obj = Solution()
print(obj.partition('aab'))