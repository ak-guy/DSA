import heapq
from collections import Counter
from typing import List


class Solution:
    """
    will use heapify all unique val in arr, then pop the first smallest val and run a loop from that val
    to (val+groupsize) and if any number is not present then we can return False else we can handle dict
    and heap accordingly
    """

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
