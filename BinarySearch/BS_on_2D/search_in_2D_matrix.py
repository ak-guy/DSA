# # Method - 1 (TC -> O(n+m))
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


# # Method - 2 (TC -> O(logn + logm) ==>> O(log(n*m)))
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        start_row = 0
        n = len(matrix)
        m = len(matrix[0]) - 1

        # first search for row like in which row our target can exist
        l, r = 0, n - 1
        search_row = -1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] == target or matrix[mid][-1] == target:
                return True
            elif matrix[mid][0] < target and matrix[mid][-1] > target:
                search_row = mid
                break
            elif matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
        # if we were not able to find the row, we will return False
        if search_row == -1:
            return False

        # Now need to search in search_row for target
        l, r = 0, m - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[search_row][mid] == target:
                return True
            elif matrix[search_row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False
