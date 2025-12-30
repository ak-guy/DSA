"""
802. Find Eventual Safe States
"""

from typing import List
from collections import deque


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        res = []
        dq = deque()
        outdegree = [0 for _ in range(n)]
        reversedGraph = [[] for _ in range(n)]

        for ind in range(n):
            for node in graph[ind]:
                reversedGraph[node].append(ind)

            outdegree[ind] = len(graph[ind])
            if outdegree[ind] == 0:
                dq.append(ind)

        while dq:
            qLen = len(dq)
            for _ in range(qLen):
                node = dq.pop()
                for neighbour in reversedGraph[node]:
                    outdegree[neighbour] -= 1
                    if outdegree[neighbour] == 0:
                        dq.append(neighbour)

        for i in range(n):
            if outdegree[i] == 0:
                res.append(i)

        return res
