class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

class Solution:
    def buildtree(self, inorder, preorder, n):
        
        # inorder -> (left, root, right)
        # preorder -> (root, left, right)
        
        def sol(pre, ino):
            if not pre and not ino:
                return None
            
            mid_val = ino.index(pre[0])
            
            root = Node(pre[0])
            
            root.left = sol(pre[1:mid_val+1], ino[:mid_val])
            root.right = sol(pre[mid_val+1:], ino[mid_val+1:])
            
            return root
            
        return sol(preorder, inorder)