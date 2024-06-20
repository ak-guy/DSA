from collections import defaultdict, deque
from typing import List, Dict

def createGraph(val1: int, val2: int, graph_type: int, gp: defaultdict):
    gp[val1].append(val2)
    if graph_type == 1:
        gp[val2].append(val1)


class DFSSolution:
    def helper(self, current_node: int, parent_node: int, graph: Dict[int, List], visited: set):
        visited.add(current_node)

        try:
            for node in graph[current_node]:
                if node not in visited:
                    if self.helper(current_node=node, parent_node=current_node, graph=graph, visited=visited):
                        return True
                elif parent_node != node:
                    return True
        except:
            return False
            
        return False

    def isCycle(self, graph: Dict[int, List]) -> bool:
        visited = set()
        for current_node in graph.keys():
            if current_node not in visited:
                if self.helper(current_node, -1, graph, visited):
                    return True
            
        return False

class BFSSolution:
    def helper(self, dq: deque, graph: Dict[int, List], visited: set):
        while dq:
            current_node, parent_node = dq.popleft()
            for node in graph[current_node]:
                if node not in visited:
                    dq.append((node, current_node))
                elif parent_node != node:
                    return True
                
                visited.add(node)
        
        return False

    def isCycle(self, graph: Dict[int, List]) -> bool:
        visited = set()
        dq = deque() # (current_node, parent_node) 
        for node in graph.keys():
            if node not in visited:
                dq.append((node, -1))
                visited.add(node)
                if self.helper(dq, graph, visited):
                    return True
        
        return False

if __name__ == '__main__':
    traversal_type = int(input("Enter integer value for traversal type dfs(0) / bfs(1) : "))
    assert traversal_type in [0,1], "Traversal Type should be 0 or 1"

    n = int(input("Enter the number of edges : "))
    assert n >= 1, "There should be atleast one node"

    gp = defaultdict(list)
    for _ in range(n):
       val1, val2 = map(int, input().split(' '))
       createGraph(val1, val2, 1, gp)
    
    print(gp)

    obj = DFSSolution() if traversal_type == 0 else BFSSolution()
    cycle_exists =  obj.isCycle(gp)
    if cycle_exists:
        print("cycle exists")
    else:
        print("no cycle found")