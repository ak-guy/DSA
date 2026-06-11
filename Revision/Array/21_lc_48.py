'''
48. Rotate Image

Intuition: The intuition behind this elegant, in-place solution is to break a complex 90∘ clockwise 
rotation down into two simpler, standard geometric transformations that completely bypass the need 
for messy coordinate calculations or extra memory. Instead of trying to shift elements directly 
into their final positions—which would trigger a complicated "musical chairs" problem of overwriting 
data—the algorithm first performs a matrix transposition, swapping elements across the main diagonal 
(matrix[r][c] with matrix[c][r]) to seamlessly convert every original row into a column. While this 
transposition successfully reorients the data grid, it leaves the columns facing the wrong direction 
(effectively creating a mirrored, anti-clockwise tilt). To correct this orientation and complete the 
clockwise rotation, the second step simply walks through the matrix row by row and reverses each 
individual row horizontally, flipping the columns from left to right into their perfect, final 
rotated positions.
'''

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_len = len(matrix)

        # step - 1: rotate anticlockwise (transpose)
        for r in range(matrix_len):
            for c in range(r, matrix_len):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        # step - 2: reverse each row
        for r in range(matrix_len):
            matrix[r].reverse()
