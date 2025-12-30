from typing import List
import heapq
from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        res = 0
        counter = Counter(arr)

        hq = []
        for key, val in counter.items():
            heapq.heappush(hq, (-val, key))

        n = len(arr)
        max_len = n / 2
        while n > max_len:
            count, num = heapq.heappop(hq)
            n += count
            res += 1
        return res
