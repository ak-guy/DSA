"""
2359. Find Closest Node to Given Two Nodes

This solution identifies the best meeting point by using a recursive DFS to pre-calculate the travel distance 
from both starting nodes to every other reachable node in the graph, storing these values in two separate 
dictionaries. Since each node has at most one outgoing edge, the DFS effectively traverses a single path 
until it hits a dead end (-1) or a cycle. After mapping all reachable distances, the code iterates through 
every possible node to find those reachable by both node1 and node2, calculating the maximum of the two 
distances for each. It then returns the node index that minimizes this maximum distance, which represents the 
point where the "slowest" traveler arrives as quickly as possible.
"""
from collections import defaultdict

class Solution:
    def dfs(self, edges: list[int], node: int, map_dict_node: dict, dist: int) -> list[int]:
        if node in map_dict_node or node == -1:
            return

        map_dict_node[node] = dist
        self.dfs(edges, edges[node], map_dict_node, dist+1)

    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        map_dict_node_1 = defaultdict(list)
        map_dict_node_2 = defaultdict(list)

        self.dfs(edges, node1, map_dict_node_1, 0)
        self.dfs(edges, node2, map_dict_node_2, 0)

        max_distance = float("inf")
        result = -1

        for i in range(len(edges)):
            if i in map_dict_node_1 and i in map_dict_node_2:
                node_1_dist = map_dict_node_1[i]
                node_2_dist = map_dict_node_2[i]

                curr_max_distance = max(node_1_dist, node_2_dist)
                if curr_max_distance < max_distance:
                    max_distance = curr_max_distance
                    result = i

        return result
