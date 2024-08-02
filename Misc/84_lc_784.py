'''
784. Letter Case Permutation
'''

from typing import List
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        res = []
        def backtrack(ind, path, path_len):
            if path_len == n:
                res.append(path)
                return

            backtrack(ind+1, path+s[ind], path_len+1)
            if s[ind].isalpha():
                backtrack(ind+1, path+s[ind].swapcase(), path_len+1)
        
        backtrack(0, '', 0)
        return res
