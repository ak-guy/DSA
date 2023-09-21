import heapq
class Solution:
    def mergeKArrays(self, arr, K):
        hq = []
        res = []
        for i in range(K):
            heapq.heappush(hq, (arr[i][0], i, 0))
        
        while hq:
            val, row, col = heapq.heappop(hq)
            res.append(val)
            if col + 1 < K:
                heapq.heappush(hq, (arr[row][col+1], row, col+1))
        
        return res