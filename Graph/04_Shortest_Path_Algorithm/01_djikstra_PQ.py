"""
Djikstra algo tells us the minimum path distance/weight we need to travel for node(anyNode) to all nodes
But it is applicable only on +ve weights
"""

import heapq

gr = {
    0: [[1, 10], [2, 1]],
    1: [[0, 10], [3, 1], [4, 1]],
    2: [[0, 1], [3, 1]],
    3: [[2, 1], [1, 1]],
    4: [[1, 1], [5, 10]],
    5: [[4, 10]],
}


def getShortestPathPossible(startNode, gr, n):
    pq = []
    heapq.heapify(pq)
    heapq.heappush(pq, [0, startNode])  # distance, node
    resArray = [float("inf") for _ in range(n)]
    resArray[startNode] = 0

    while pq:
        distance, node = heapq.heappop(pq)

        for neighbour in gr[node]:
            neighbourNode = neighbour[0]
            weight = neighbour[1]
            if distance + weight < resArray[neighbourNode]:
                resArray[neighbourNode] = distance + weight
                heapq.heappush(pq, [distance + weight, neighbourNode])

    print(resArray)


if __name__ == "__main__":
    getShortestPathPossible(0, gr, 6)
