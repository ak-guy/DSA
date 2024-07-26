'''
861. Score After Flipping Matrix
'''

from typing import List
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        '''
        to achieve highest score we need to make first bit (from left) equal to 1
        (bcz 1000 will always be bigger than 0111)

        so min res that we can obtain from any matrix is (1 << (n-1)) * m
        where m = no_of_rows and n = no_of_cols

        now we need to check all col from 1 to n and see what max val we can obtain from there
        so now val will be like 1 << (n-1-1), 1 << (n-1-2), 1 << (n-1-3), ...so on till 1 << (n-1-n-1)

        '''
        m = len(grid)
        n = len(grid[0])

        res = (1 << (n-1)) * m

        for col in range(1, n):
            match_bits = sum(grid[row][0] == grid[row][col] for row in range(m))
            # match_bits will help us in knowing whether we have to flip the col bit values or not

            res += max(match_bits, m-match_bits) * (1 << n-1-col)
        
        return res