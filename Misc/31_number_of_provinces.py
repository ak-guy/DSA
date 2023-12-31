from typing import List
from collections import defaultdict, deque
class Solution:
    def makeGraph(self, isConnected: List[List[int]], n: int):
        gr = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if isConnected[i][j] == 1:
                    gr[i].append(j)
        return gr

    def markConnectedCities(self, graph, ind, visited) -> None:
        q = deque()
        q.append(ind)
        while q:
            i = q.popleft()
            if visited[i] == 0:
                for inds in graph[i]:
                    q.append(inds)
            visited[i] = 1

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        res = 0
        visited = [0 for city in range(n)]
        graph = self.makeGraph(isConnected, n)
        for i in range(n):
            if visited[i] == 0:
                res += 1
                self.markConnectedCities(graph, i, visited)
        
        return res