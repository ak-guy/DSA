"""
1042. Flower Planting With No Adjacent

This solution addresses the graph coloring problem by combining an adjacency list representation with a Breadth-First Search (BFS)
traversal that accounts for disconnected components. It iterates through every garden from 1 to n, initiating a BFS whenever it
encounters an uncolored node to ensure every "island" in the graph is processed. For each node, the algorithm identifies available
colors by checking its neighbors' current assignments, picks one of the remaining four colors greedily, and then queues any
unvisited neighbors to continue the traversal. By using a n+1 sized array and returning a slice, it cleanly maps the problem's
1-based garden indexing to Python's 0-based list structure.
"""

from collections import defaultdict, deque

"""Using BFS"""


class Solution:
    def makeModifiedGraph(self, paths: list[list[int]]) -> dict:
        graph = defaultdict(list)
        for i in range(len(paths)):
            graph[paths[i][0]].append(paths[i][1])
            graph[paths[i][1]].append(paths[i][0])

        return graph

    def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:
        graph = self.makeModifiedGraph(paths)
        result = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            if result[i] == 0:
                q = deque([i])
                while q:
                    curr_node = q.popleft()
                    possibilities = set([1, 2, 3, 4])
                    for neighbour in graph[curr_node]:
                        if result[neighbour] == 0:
                            q.append(neighbour)
                        possibilities.discard(result[neighbour])

                    result[curr_node] = possibilities.pop()

        return result[1:]


"""Using normal iteration"""


class Solution2:
    def makeModifiedGraph(self, paths: list[list[int]]) -> dict:
        graph = defaultdict(list)
        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)

        return graph

    def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:
        graph = self.makeModifiedGraph(paths)
        result = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            neighbours_plants = set([result[neighbour] for neighbour in graph[i]])
            for possible_plants in range(1, 5):
                if possible_plants not in neighbours_plants:
                    result[i] = possible_plants

        return result[1:]
