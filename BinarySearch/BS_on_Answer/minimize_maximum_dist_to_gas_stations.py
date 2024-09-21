# # Kinda brute force
import heapq
class Solution:
    def findSmallestMaxDist(self, stations, K):
        n = len(stations)
        pq = []
        no_gas_station_bw_interval = [0 for i in range(n-1)] # this we will use to maintain the positions where we had built gas station
        
        for i in range(n-1): # TC -> nlogn && SC -> n-1
            heapq.heappush(pq, (-1 * (stations[i+1]-stations[i]), i)) # taking negative to convert it to maxheap
        
        for k in range(1,K+1): # TC -> Klogn
            val = heapq.heappop(pq)
            dist = val[0]
            ind = val[1]
            
            no_gas_station_bw_interval[ind] += 1
            gap = stations[ind + 1] - stations[ind]
            new_dist = gap / (no_gas_station_bw_interval[ind] + 1)
            
            heapq.heappush(pq, (-1 * (new_dist), ind))
        
        res = pq[0][0] * (-1)
        return res
    
# # Binary Search -> this does not submit on gfg but approach is correct
class Solution:
    def getRequiredGasStations(self, stations, min_dist_needed_to_be_satisfied, n):
        used_gas_stations = 0
        for i in range(n-1):
            required_gas_station = (stations[i+1] - stations[i]) / min_dist_needed_to_be_satisfied
            if stations[i+1] - stations[i]  == required_gas_station * min_dist_needed_to_be_satisfied:
                required_gas_station -= 1
            used_gas_stations += required_gas_station
        
        return used_gas_stations
                
    def findSmallestMaxDist(self, stations, K):
        n = len(stations)
        l = 0
        r = 0 # some dummy value
        res = 1000000007
        for i in range(n-1):
            r = max(r, stations[i+1] - stations[i])
        
        while r - l > 10**(-6):
            mid = (l + r) / 2
            gas_stations = self.getRequiredGasStations(stations, mid, n)
            
            if gas_stations <= K:
                res = min(res, mid)
                r = mid
            else:
                l = mid
        
        return res