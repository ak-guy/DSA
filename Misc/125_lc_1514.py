'''
1514. Path with Maximum Probability
'''
import heapq
from collections import defaultdict
from typing import List
class Solution:
    def makeGraph(self, n, edges, succProb):
        gp = defaultdict(list)
        for i in range(len(edges)):
            gp[edges[i][0]].append([edges[i][1], succProb[i]])
            gp[edges[i][1]].append([edges[i][0], succProb[i]])
        
        return gp

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        maxProbability = [0.00000 for _ in range(n)]
        gp = self.makeGraph(n, edges, succProb)

        pq = []
        heapq.heapify(pq)
        heapq.heappush(pq, [-1.00000, start_node])

        while pq:
            prob, node = heapq.heappop(pq)
            prob = abs(prob)
            for neighbour in gp[node]:
                neighbourNode = neighbour[0]
                neighbourProb = neighbour[1]

                if prob * neighbourProb > maxProbability[neighbourNode]:
                    maxProbability[neighbourNode] = prob * neighbourProb
                    heapq.heappush(pq, [-1 * prob * neighbourProb, neighbourNode])
        # print(maxProbability)
        return maxProbability[end_node]