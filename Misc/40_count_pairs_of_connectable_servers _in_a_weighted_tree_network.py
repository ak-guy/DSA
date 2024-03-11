# # please ignore this submission
from __future__ import annotations

import collections
from typing import List


class Solution:
    def countPairsOfConnectableServers(self, edges: list[list[int]], signalSpeed: int) -> list[int]:
        no_of_edges = len(edges) + 1
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append([edge[1], edge[2]])
            graph[edge[1]].append([edge[0], edge[2]])

        res_array = [0 for i in range(no_of_edges)]

        for root_node in graph.keys():
            count_array = []  # this will keep count of number of nodes for each subgraph which has distance divisble by signalSpeed
            for subgraph in graph[root_node]:
                visited = [0 for i in range(no_of_edges)]
                count = 0

                def dfs(signalSpeed, root_node, subgraph, graph, visited, distance):
                    nonlocal count
                    if visited[subgraph[0]] == 1:
                        return 0
                    visited[subgraph[0]] = 1
                    count = 1 if distance % signalSpeed == 0 else 0
                    for sub_graphs in graph[subgraph[0]]:
                        count += dfs(signalSpeed, root_node=subgraph[0], subgraph=sub_graphs,
                                     graph=graph, visited=visited, distance=distance+sub_graphs[1])
                    return count

                visited[root_node] = 1
                get_no_of_nodes_that_satisfies_condition = dfs(
                    signalSpeed, root_node, subgraph, graph, visited, subgraph[1])
                count_array.append(get_no_of_nodes_that_satisfies_condition)

            total_nodes = sum(count_array)
            res = 0
            for no_of_nodes in count_array:
                res += no_of_nodes**2
            res = (total_nodes**2 - res)/2
            res_array[root_node] = int(res)

        return res_array
