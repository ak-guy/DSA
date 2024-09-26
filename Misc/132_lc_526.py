'''
526. Beautiful Arrangement
'''

class Solution:
    def countArrangement(self, n: int) -> int:
        res = 0
        def helper(currIndex, n, used):
            nonlocal res
            # base case
            if currIndex>n:
                res += 1
                return

            for numberToPut in range(1, n+1):
                if used[numberToPut] == 0 and (numberToPut%currIndex==0 or currIndex%numberToPut==0):
                    used[numberToPut] = 1
                    helper(currIndex+1,n,used)
                    used[numberToPut] = 0

        used = [0 for _ in range(n+1)]
        helper(1, n , used)
        return res