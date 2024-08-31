"""
767. Reorganize String
"""

from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        pq = []
        heapq.heapify(pq)

        for key, val in counter.items():
            heapq.heappush(pq, (-1*val, key))
        
        res = ''
        while len(pq) > 0:
            first = heapq.heappop(pq) # -ve int: string 
            if (res != '' and first[1] == res[-1]):
                try:
                    second = heapq.heappop(pq)
                except IndexError:
                    return ''
                res += second[1]
                heapq.heappush(pq, first)
                if abs(second[0]) > 1:
                    heapq.heappush(pq, (second[0]+1, second[1]))
            else:
                res += first[1]
                if abs(first[0]) > 1:
                    heapq.heappush(pq, (first[0]+1, first[1]))
        
        return res