'''
pretty straight forward problem
'''

from typing import List
class Solution:
    def helper(self, ind: int, k: int, n: int, instance: List, res: List):
        if n < 0 or k < 0:
            return
        if n == 0 and k == 0:
            res.append(instance.copy())
            return

        for i in range(ind, 9):
            instance.append(i+1)
            self.helper(i+1, k-1, n-i-1, instance, res)
            
            # backtrack
            instance.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.helper(0,k,n,[], res)
        return res