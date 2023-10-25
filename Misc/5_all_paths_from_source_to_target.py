# # Method - 1 (BFS)
from typing import List
from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        q = deque()
        q.append([0])

        while q:
            path = q.popleft()
            if path[-1] == n-1:
                res.append(path)
            else:
                for val in graph[path[-1]]:
                    q.append(path + [val])
        
        return res
        

# # Method - 2 (DFS Iterative)