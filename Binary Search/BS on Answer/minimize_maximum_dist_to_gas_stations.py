# # Kinda brute force
import heapq
class Solution:
    def findSmallestMaxDist(self, stations, K):
        n = len(stations)
        pq = []
        no_gas_station_bw_interval = [0 for i in range(n-1)]
        
        for i in range(n-1): # TC -> nlogn && SC -> n-1
            heapq.heappush(pq, (-1 * (stations[i+1]-stations[i]), i)) # taking negative to convert it to maxheap
        
        for k in range(1,K+1):
            val = heapq.heappop(pq)
            dist = val[0]
            ind = val[1]
            
            no_gas_station_bw_interval[ind] += 1
            dist = stations[ind + 1] - stations[ind]
            dist = dist / (no_gas_station_bw_interval[ind] + 1)
            
            heapq.heappush(pq, (-1 * (dist), ind))
        
        res = pq[0][0] * (-1)
        return res
    
# # Binary Search
