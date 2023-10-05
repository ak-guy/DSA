# # Method - 1 (Using sorted function)
class Solution:
    def replaceWithRank(self, N, arr):
        new_arr = sorted(arr)
        rank = 1
        dic = {}
        for i in range(N):
            if new_arr[i] not in dic:
                dic[new_arr[i]] = rank
                rank += 1
        
        for i in range(N):
            arr[i] = dic[arr[i]]
        
        return arr
    
# # Method - 2 (Using heaps)
'''
algo: store (val, ind) in minheap, pop one by one then go to ind and give it rank, and to rank should be
      increased only if prev_val is not equal to current popped value
'''
import heapq
class Solution:
    def replaceWithRank(self, N, arr):
        hq = []
        rank = 0
        for i in range(N):
            heapq.heappush(hq, (arr[i], i))
        
        prev_val = 0
        while hq:
            val, i = heapq.heappop(hq)
            if val != prev_val:
                rank += 1
            arr[i] = rank
            prev_val = val
        
        return arr