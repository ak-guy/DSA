class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        start_row = 0
        n = len(matrix)
        start_col = len(matrix[0]) - 1
        while start_row < n and start_col >= 0:
            if matrix[start_row][start_col] == target:
                return True
            elif matrix[start_row][start_col] > target:
                start_col -= 1
            else:
                start_row += 1
        
        return False