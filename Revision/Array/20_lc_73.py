'''
73. Set Matrix Zeroes

Intuition: The intuition behind this highly optimized, space-efficient solution is to treat the 
very first row and column of the matrix as a built-in tracking billboard, using the matrix's own 
real estate instead of allocating extra memory. Because modifying cells mid-scan would cause a 
catastrophic chain reaction of accidental zeroes, the algorithm uses a two-pass strategy: a 
forward pass to look for zeroes and flag their locations, and a backward pass to actually execute 
the wipeout. During the forward pass, if an inner cell is zero, its respective row header 
(matrix[i][0]) and column header (matrix[0][j]) are marked with a 0. To prevent a tracking collision 
at the overlapping top-left corner (matrix[0][0]), the first row's fate is tied to that corner, 
while the first column's fate is safely isolated inside a dedicated boolean variable (set_col_zero_0). 
Finally, the second pass moves backward from the bottom-right to safely update the inner cells using 
the header flags without prematurely overwriting the billboard before lower rows have a chance to 
read it, wrapping up by using the tracking variable to wipe out the first column last.
'''

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len, col_len = len(matrix), len(matrix[0])
        set_col_zero_0 = False

        for i in range(row_len):
            if matrix[i][0] == 0:
                set_col_zero_0 = True
            for j in range(1, col_len):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(row_len-1,-1,-1):
            for j in range(col_len-1,0,-1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

            if set_col_zero_0:
                matrix[i][0] = 0
