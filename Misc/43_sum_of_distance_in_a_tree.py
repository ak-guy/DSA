# # brute force (run dfs on each node and get total distance)
from typing import List
from collections import defaultdict
class Solution:
    def dfs(self, node, graph, visited, distance):
        if visited[node] == 1:
            return 0
        visited[node] = 1
        total_distance = distance
        for nodes in graph[node]:
            total_distance += self.dfs(nodes, graph, visited, distance=distance+1)
        return total_distance

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        res = []
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        for node in range(n):
            visited = [0 for i in range(n)]
            total_distance_for_node = self.dfs(node, graph, visited, 0)
            # print(f"total distance for node {node} is {total_distance_for_node}")
            res.append(total_distance_for_node)
        return res
    
# # Optimized Approach
