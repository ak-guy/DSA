from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dummy_matrix = [[1 for i in range(n)] for j in range(n)]

        """
        rb -> row begining
        re -> row end
        cb -> column begining
        ce -> column end
        """
        rb, re, cb, ce = 0, n - 1, 0, n - 1

        value_to_be_entered = 1
        while rb <= re and cb <= ce:
            for i in range(cb, ce + 1):  # going left to right
                dummy_matrix[rb][i] = value_to_be_entered
                value_to_be_entered += 1

            for i in range(rb + 1, re + 1):  # going top to bottom
                dummy_matrix[i][ce] = value_to_be_entered
                value_to_be_entered += 1

            if rb != re:
                for i in range(ce - 1, cb - 1, -1):  # going right to left
                    dummy_matrix[re][i] = value_to_be_entered
                    value_to_be_entered += 1

            if cb != ce:
                for i in range(re - 1, rb, -1):  # going bottom to top
                    dummy_matrix[i][cb] = value_to_be_entered
                    value_to_be_entered += 1

            rb += 1
            re -= 1
            cb += 1
            ce -= 1

        return dummy_matrix
