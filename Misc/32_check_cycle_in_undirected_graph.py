from __future__ import annotations

from typing import List


class Solution:
    def dfs(self, current_node, parent_node, adj: list[list[int]], visited: list[int]) -> int:
        visited[current_node] = 1

        for destination_node in adj[current_node]:
            if visited[destination_node] == 0:
                if self.dfs(destination_node, current_node, adj, visited):
                    return True
            elif destination_node != parent_node:
                return True

        return False

    def isCycle(self, V: int, adj: list[list[int]]) -> bool:
        visited = [0 for i in range(V)]

        for i in range(V):
            if visited[i] == 0:
                if self.dfs(i, -1, adj, visited):
                    return True
        return False
