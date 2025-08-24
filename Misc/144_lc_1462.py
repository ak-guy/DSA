'''
1462. Course Schedule IV
'''

# Method - 1
'''
This code solves LeetCode problem 1462 "Course Schedule IV" using a 
graph-based approach with depth-first search (DFS). The solution 
builds a reverse prerequisite graph where each course points to 
all courses that depend on it, then uses DFS from each course to 
determine all courses that can be reached (meaning all courses 
for which the current course is a prerequisite). The main algorithm
creates a 2D boolean matrix to track reachability between all 
course pairs, performs DFS traversal from each course to populate 
this matrix, and finally answers the queries by checking if one 
course is a prerequisite of another using the precomputed 
reachability information. The time complexity is 
O(numCourses² + numCourses * edges) due to running DFS from each 
course, making it suitable for scenarios where multiple queries 
need to be answered efficiently about prerequisite relationships.
'''

from collections import defaultdict
from typing import List

class Solution:
    def makeGraph(self, nodes: List[List[int]]) -> dict[int, List[int]]:
        graph = defaultdict(list)
        for node in nodes:
            graph[node[1]].append(node[0])
        
        return graph

    def dfs_traversal(self, start_node: int, current_node: int, graph: dict[int, List[int]], visited: List[bool], possible_to_reach: List[List[bool]]):
        if visited[current_node]:
            return

        visited[current_node] = True

        for node in graph[current_node]:
            possible_to_reach[start_node][node] = True
            self.dfs_traversal(start_node, node, graph, visited, possible_to_reach)

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = self.makeGraph(prerequisites)

        possible_to_reach = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        for i in range(numCourses):
            visited = [False for _ in range(numCourses)]
            self.dfs_traversal(i, i, graph, visited, possible_to_reach)

        result = []
        for q in queries:
            if possible_to_reach[q[1]][q[0]]:
                result.append(True)
            else:result.append(False)

        return result

# # Method - 2 (Using topological sorting)
'''
This solution to LeetCode 1462 uses a topological sort on the course
prerequisite graph to determine all direct and indirect prerequisites 
for each course. It builds an indegree array and a graph from the 
prerequisites, then processes courses with zero indegree in a queue, 
propagating prerequisite information by merging sets of prerequisites 
from each course to its neighbors. After this preprocessing, it 
efficiently answers queries by checking if one course appears as a 
prerequisite in the recorded sets of another. This approach allows 
quick determination of prerequisite relationships for multiple queries 
after a single traversal.
'''
from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegree = [0 for _ in range(numCourses)]
        graph = defaultdict(list)
        for prerequisite in prerequisites:
            graph[prerequisite[0]].append(prerequisite[1])
            indegree[prerequisite[1]] += 1
        
        dq = deque()
        for ind in range(numCourses):
            if indegree[ind] == 0:
                dq.append(ind)

        prerequisite_nodes = defaultdict(set)
        while dq:
            node = dq.popleft()
            for neighbour in graph[node]:
                prerequisite_nodes[neighbour].add(node)
                for dependent_nodes in prerequisite_nodes[node]:
                    prerequisite_nodes[neighbour].add(dependent_nodes)

                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    dq.append(neighbour)

        result = []
        for query in queries:
            if query[0] in prerequisite_nodes[query[1]]:
                result.append(True)
                continue
            result.append(False)
        
        return result
