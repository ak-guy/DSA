'''this module takes input from user and creates a graph(Directed/Undirected Cyclic/Acyclic Graph with single component),
   and then takes a starting node and traverses on that graph in BFS manner
'''
from collections import defaultdict, deque
from typing import List
import sys

def createGraph(val1: int, val2: int, graph_type: int, gp: defaultdict):
    gp[val1].append(val2)
    if graph_type == 1:
        gp[val2].append(val1)

def bfsTraversal(startnode: int, gp: defaultdict) -> List[int]:
    q = deque()
    q.append(startnode)
    res = []
    visited = set()
    visited.add(startnode)
    while q:
        node = q.popleft()
        res.append(node)
        for child_node in gp[node]:
            if child_node not in visited:
                visited.add(child_node)
                q.append(child_node)
            
    return res

def dfsTraversal(startnode: int, gp: defaultdict) -> List[int]:
    res = []
    visited = set()
    
    def helper(node):
        res.append(node)
        visited.add(node)
        for child_node in gp[node]:
            if child_node not in visited:
                helper(child_node)

    helper(startnode)
    return res

if __name__ == '__main__':
    graph_type = int(input("Enter integer value for graph type directed(0) / undirected(1) : "))
    assert graph_type in [0,1], "Graph type should be either 0 or 1"

    n = int(input("Enter the number of edges : "))
    assert n >= 1, "There should be atleast one edge"

    gp = defaultdict(list)
    for _ in range(n):
        try:
            val1, val2 = map(int, input().split(' '))
            createGraph(val1, val2, graph_type, gp)
        except Exception as e:
            print("more than two values provided >> {}".format(e))
            sys.exit(0)
            
    print(gp) # for debugging

    startnode = int(input("Enter starting node : "))
    if startnode not in gp.keys():
        startnode = int(input("Entered startnode does not exist in graph, Please enter correct starting node : "))

    final_bfs_traversal = bfsTraversal(startnode, gp)
    final_dfs_traversal = dfsTraversal(startnode, gp)
    print(*final_bfs_traversal)
    print(*final_dfs_traversal)