'''
378. Kth Smallest Element in a Sorted Matrix
'''

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