'''
1481. Least Number of Unique Integers after K Removals
'''
import heapq
from typing import List
class CustomComparator:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        numberVsCount = {}
        for val in arr:
            numberVsCount[val] = 1 + numberVsCount.get(val, 0)
        
        pq = []
        heapq.heapify(pq)
        for key, val in numberVsCount.items():
            heapq.heappush(pq, CustomComparator(key, val))
        
        while k:
            top = pq[0]
            if top.value <= k:
                heapq.heappop(pq)
                k -= top.value
            else:
                break
                
        return len(pq)