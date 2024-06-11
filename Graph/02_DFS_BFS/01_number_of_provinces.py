'''
test
'''
from typing import List
from collections import deque

class Solution:
    def traverseAndMarkVisitedCities(self, visited: set, city:int, isConnected: List[List[int]], n: int) -> None:
        q = deque()
        visited.add(city)
        q.append(city)
        while q:
            current_city = q.popleft()
            for i in range(n):
                if isConnected[current_city-1][i] == 1 and i+1 not in visited:
                    q.append(i+1)
                    visited.add(i+1)


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        for city in range(1, n+1):
            if city not in visited:
                self.traverseAndMarkVisitedCities(visited, city, isConnected, n)
                provinces += 1

        return provinces