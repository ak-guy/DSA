from collections import defaultdict
class Solution:
    
    def KDistanceNodes(self,root,target,k):
        # code here
        # return the sorted list all nodes at k distance from target
        gr = defaultdict(list)
        
        def makeGraph(root, prev):
            if not root:
                return
            
            if prev:
                gr[root.data].append(prev)
            if root.left:
                gr[root.data].append(root.left.data)
            if root.right:
                gr[root.data].append(root.right.data)
                
            makeGraph(root.left, root.data)
            makeGraph(root.right, root.data)
        
        makeGraph(root, None)
        
        # applying bfs, instead of using queue we will use set to mark visited nodes
        res = [target]
        visited = set(res)
        for i in range(k):
            new_result = []
            for parent_node in res:
                for child_node in gr[parent_node]:
                    if child_node not in visited:
                        new_result.append(child_node)
            res = new_result
            visited |= set(res)
        
        return sorted(res)