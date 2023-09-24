import heapq
from collections import Counter
from typing import List
class Solution:
    def isPossibleDivide(self, hand: List[int], groupSize: int) -> bool:
        dic = Counter(hand)
        hq = [val for val in dic.keys()]
        heapq.heapify(hq)

        while hq:
            mini = hq[0]

            for val in range(mini, groupSize + mini):
                if val not in dic:
                    return False
                
                dic[val] -= 1
                if dic[val] == 0:
                    heapq.heappop(hq)
            
        return True