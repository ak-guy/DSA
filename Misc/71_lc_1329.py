"""
1329. Sort the Matrix Diagonally
"""

from typing import List
import heapq


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        hmap = {}  # int_representing_matrix_diagonal : heap

        for r in range(n):
            for c in range(m):
                if c - r in hmap:
                    heapq.heappush(hmap[c - r], mat[r][c])
                else:
                    hq = []
                    heapq.heappush(hq, mat[r][c])
                    hmap.update({c - r: hq})

        for r in range(n):
            for c in range(m):
                mat[r][c] = heapq.heappop(hmap[c - r])

        return mat
