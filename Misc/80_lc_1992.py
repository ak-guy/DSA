"""
1992. Find All Groups of Farmland
"""

from collections import deque
from typing import List


class Solution:
    def getGroup(self, r: int, c: int, land: List[List[int]], n: int, m: int):
        q = deque()
        q.append((r, c))
        start_point = (r, c)
        end_point = (r, c)
        land[r][c] = 0

        while q:
            row, col = q.popleft()
            directions = [[0, 1], [1, 0]]
            for direction in directions:
                new_r = row + direction[0]
                new_c = col + direction[1]
                if new_r < n and new_c < m and land[new_r][new_c] == 1:
                    q.append((new_r, new_c))
                    total = end_point[0] + end_point[1]
                    new_total = new_r + new_c

                    if new_total >= total:
                        end_point = (new_r, new_c)
                    land[new_r][new_c] = (
                        0  # resetting farmland to forestland to avoid encountering it again
                    )

        return [start_point[0], start_point[1], end_point[0], end_point[1]]

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n = len(land)
        m = len(land[0])
        res = []

        for r in range(n):
            for c in range(m):
                if land[r][c] == 1:
                    res.append(self.getGroup(r, c, land, n, m))

        return res
