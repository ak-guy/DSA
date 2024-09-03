'''
1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
'''

import heapq
from typing import List
class Solution:
    def getMinimumCitiesReachable(self, city, gr, distanceThreshold, n):
        resArray = [float("inf") for _ in range(n)]
        reachableCity = [False for _ in range(n)]
        res = 0
        pq = []
        heapq.heapify(pq)
        heapq.heappush(pq, [0, city])
        resArray[city] = 0

        while pq:
            distanceTravelled, node = heapq.heappop(pq)
            for it in gr[node]:
                neighbourNode = it[0]
                weight = it[1]
                if distanceTravelled + weight < resArray[neighbourNode]:
                    resArray[neighbourNode] = distanceTravelled + weight
                    if not reachableCity[neighbourNode] and resArray[neighbourNode] <= distanceThreshold: 
                        res += 1
                        reachableCity[neighbourNode] = True
                    heapq.heappush(pq, [resArray[neighbourNode], neighbourNode])
        return res

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        gr = {}
        for edge in edges:
            if not gr.get(edge[0]): gr[edge[0]] = [[edge[1], edge[2]]]
            else: gr[edge[0]].append([edge[1], edge[2]])

            if not gr.get(edge[1]): gr[edge[1]] = [[edge[0], edge[2]]]
            else: gr[edge[1]].append([edge[0], edge[2]])
        
        minCitiesReachable = 1_000_000_000
        res = 0
        for city in range(n):
            citiesReachable = self.getMinimumCitiesReachable(city, gr, distanceThreshold, n) if city in gr else 0
            minCitiesReachable = min(minCitiesReachable , citiesReachable)
            if citiesReachable <= minCitiesReachable:
                res = city

        return res