'''
885. Spiral Matrix III
'''

from typing import List
class Solution:
    def isValid(self, r: int, c: int, n: int, m: int, res: List[int]) -> int:
        ''' returns 1 if we are visiting valid position in spiral matrix '''
        if 0 <= r < n and 0 <= c < m:
            res.append([r,c])
            return 1
        return 0
        

    def spiralMatrixIII(self, n: int, m: int, row: int, col: int) -> List[List[int]]:
        res_count = 1
        total_count = n * m
        res = [[row, col]]
        x, y = 1, 2
        while res_count < total_count:
            # going left to right, x steps at a time
            for _ in range(x):
                col += 1
                res_count += self.isValid(row, col, n, m, res)
            
            # going top to bottom, x steps at a time
            for _ in range(x):
                row += 1
                res_count += self.isValid(row, col, n, m, res)

            # going right to left, y steps at a time
            for _ in range(y):
                col -= 1
                res_count += self.isValid(row, col, n, m, res)
                
            # going bottom to top, y steps at a time
            for _ in range(y):
                row -= 1
                res_count += self.isValid(row, col, n, m, res)

            x += 2
            y += 2

        return res