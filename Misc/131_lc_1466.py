'''
1466. Reorder Routes to Make All Paths Lead to the City Zero
'''

from typing import List
from collections import deque, defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        directedGraph = defaultdict(list)
        undirectedGraph = defaultdict(list)
        for fromCity, toCity in connections:
            directedGraph[fromCity].append(toCity)

            undirectedGraph[fromCity].append(toCity)
            undirectedGraph[toCity].append(fromCity)

        res = 0
        q = deque()
        q.append(0)
        visited = set()
        visited.add(0)

        while q:
            qSize = len(q)
            for i in range(qSize):
                fromCity = q.popleft()
                for toCity in undirectedGraph.get(fromCity, []):
                    if toCity not in visited:
                        if fromCity not in directedGraph.get(toCity, []):
                            res+=1
                        q.append(toCity)
                        visited.add(toCity)
                    
        
        return res