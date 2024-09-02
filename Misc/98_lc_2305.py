'''
2305. Fair Distribution of Cookies
'''
from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        arr = [0 for _ in range(k)]
        n = len(cookies)
        res = 1_000_000_000
        
        def rec(i):
            nonlocal res
            if i == n:
                arrMax = max(arr)
                res = min(res, arrMax)
                return
            
            for ind in range(k):
                if arr[ind] + cookies[i] < res:
                    arr[ind] += cookies[i]
                    rec(i+1)
                    arr[ind] -= cookies[i]

        rec(0)
        return res
