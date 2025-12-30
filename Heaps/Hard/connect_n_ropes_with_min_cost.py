import heapq


class Solution:
    """
    pretty straight forward, if we want to keep the cost low then we have pick smaller numbers
    """

    def minCost(self, arr, n):
        heapq.heapify(arr)
        res = 0

        while len(arr) > 1:
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            res += first + second
            heapq.heappush(arr, first + second)

        return res
