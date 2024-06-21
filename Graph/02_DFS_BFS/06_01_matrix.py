from collections import deque
from typing import List

'''
Brute Force (BFS) (TLE) : 
'''
class Solution:
    def getDistance(self, r: int, c: int, mat: List[List[int]], n: int, m: int, distance: int=0) -> int:
        visited = set()
        visited.add((r,c))
        dq = deque()
        dq.append((r, c, distance))
        res = 1_000_000_000
        while dq:
            r, c, distance = dq.popleft()
            directions = [[0,1], [1,0], [-1,0], [0,-1]]
            for direction in directions:
                row = r + direction[0]
                col = c + direction[1]
                if row < 0 or row >= n or col < 0 or col >= m:
                    continue
                    
                if (row, col) not in visited:
                    dq.append((row, col, distance+1))
                    visited.add((row, col))

            if mat[r][c] == 0:
                res = min(res, distance)
        return res

        
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        res = [[0 for i in range(m)] for j in range(n)]
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 1:
                    res[r][c] = self.getDistance(r, c, mat, n, m)
        
        return res
    
'''
BFS : will use multi-source bfs (will put all (r,c) in deque where value is 0 
      then expand and mark lowest possible distance to all 1's)
'''

class Solution:
    def markNearestDistance(self, dq: deque, mat: List[List[int]], n: int, m: int, res: List[List[int]]) -> None:
        while dq:
            r, c, distance = dq.popleft()

            directions = [[0,1], [1,0], [-1,0], [0,-1]]
            for direction in directions:
                row = r + direction[0]
                col = c + direction[1]
                if 0 <= row < n and 0 <= col < m and res[row][col] > res[r][c] + 1:
                    dq.append((row, col, distance+1))
                    res[row][col] = res[r][c] + 1
        
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        res = [[0 for i in range(m)] for j in range(n)]

        dq = deque() # row, col, distance
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 0:
                    dq.append((r,c,0))
                else:
                    res[r][c] = 1_000_000
        
        self.markNearestDistance(dq, mat, n, m, res)
        
        return res