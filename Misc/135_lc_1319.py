'''
1319. Number of Operations to Make Network Connected
'''

from typing import List
class Solution:
    def dfs(self, node, gr, visited):
        visited[node] = 1
        for neighbour in gr[node]:
            if visited[neighbour] == 0:
                self.dfs(neighbour, gr, visited)

    def findTotalComponents(self, n, gr):
        total = 0
        visited = [0 for _ in range(n)]
        for i in range(n):
            if visited[i] == 0:
                self.dfs(i, gr, visited)
                total += 1

        return total

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        totalConnections = len(connections)
        if totalConnections < n-1:
            return -1

        graph = {i:[] for i in range(n)}

        for connection in connections:
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
        # print(graph)
        
        return self.findTotalComponents(n, graph) - 1