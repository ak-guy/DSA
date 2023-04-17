# # passing 33/94 cases (giving segmenatation fault error) -> but solution is correct

import copy, sys
sys.setrecursionlimit(1000000)

class Solution:
    def printBoundaryView(self, root):
        # Code here
        res = [root.data]
        
        if not root.left and not root.right:
            return res
        
        var1 = copy.deepcopy(root)
        var2 = copy.deepcopy(root)
        
        def left_tree(root):
            if not root or (not root.left and not root.right):
                return 
            
            res.append(root.data)
            
            if root.left:
                left_tree(root.left)
            else:
                left_tree(root.right)
            return
        
        if var1.left:
            left_tree(var1.left)

        def bottom_tree(root):
            if not root:
                return
            
            bottom_tree(root.left)
            if not root.left and not root.right:
                res.append(root.data)
            bottom_tree(root.right)
            return
        
        bottom_tree(var2)

        def right_tree(root):
            if not root or (not root.left and not root.right):
                return
            
            if root.right:
                right_tree(root.right)
            else:
                right_tree(root.left)
            
            res.append(root.data)
            return
        
        if root.right:
            right_tree(root.right)
        
        return res