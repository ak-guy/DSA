"""
378. Kth Smallest Element in a Sorted Matrix
"""

import heapq
from typing import List


# Method -1 : Brute force
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = []
        heapq.heapify(pq)
        heapLen = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                heapq.heappush(pq, -1 * matrix[r][c])
                heapLen += 1
                if heapLen > k:
                    heapq.heappop(pq)
                    heapLen -= 1

        return -1 * (heapq.heappop(pq))


# Method - 2 : Binary Search
# Binary Search
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])

        def smallerOrEqualCount(val):
            res = 0
            colEnd = m - 1
            for r in range(n):
                while colEnd >= 0 and matrix[r][colEnd] > val:
                    colEnd -= 1
                res += colEnd + 1

            return res

        # search range
        start, end = matrix[0][0], matrix[n - 1][m - 1]
        ans = 0
        while start <= end:
            toSearch = (end + start) // 2
            if smallerOrEqualCount(toSearch) >= k:
                ans = toSearch
                end = toSearch - 1
            else:
                start = toSearch + 1

        return ans
