from typing import List
from collections import defaultdict
import heapq


class Solution:
    def makeGraph(self, points: List[List[int]], n: int):
        """
        imput, points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
        output, graph = {0: [(4, 1), (13, 2), (7, 3), (7, 4)],
                         1: [(4, 0), (9, 2), (3, 3), (7, 4)],
                         2: [(13, 0), (9, 1), (10, 3), (14, 4)],
                         3: [(7, 0), (3, 1), (10, 2), (4, 4)],
                         4: [(7, 0), (7, 1), (14, 2), (4, 3)]}
        """
        manhattan_distance = lambda x1, x2: abs(x1[0] - x2[0]) + abs(x1[1] - x2[1])
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                d = manhattan_distance(points[i], points[j])
                graph[i].append((d, j))
                graph[j].append((d, i))

        return graph

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = self.makeGraph(points, n)  # Dict[int : List[Tuple[int]]]
        visited = [0 for i in range(n)]  # 0 -> not_visited, 1 -> visited
        visited[0] = 1
        visited_count = 0  # will break out as soon as we visit all nodes
        min_sum = 0  # this will store the result (mst value)
        hq = graph[0]  # list
        heapq.heapify(hq)
        while hq:
            distance, node = heapq.heappop(
                hq
            )  # will pick out the minimum distance value
            if visited[node] == 0:
                visited[node] = 1
                visited_count += 1
                min_sum += distance
                for val in graph[node]:
                    heapq.heappush(hq, val)
            if visited_count == n:
                break

        return min_sum
