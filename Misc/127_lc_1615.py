"""
1615. Maximal Network Rank
"""

from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        existingRoads = set()
        nodeVsNeighbourCount = [0 for _ in range(n)]
        for road in roads:
            existingRoads.add((road[0], road[1]))
            nodeVsNeighbourCount[road[0]] += 1
            nodeVsNeighbourCount[road[1]] += 1

        res = 0
        for city1 in range(n - 1):
            for city2 in range(city1 + 1, n):
                count = nodeVsNeighbourCount[city1] + nodeVsNeighbourCount[city2]
                if (city1, city2) in existingRoads or (city2, city1) in existingRoads:
                    count -= 1

                res = max(res, count)

        return res
