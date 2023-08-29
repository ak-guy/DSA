# # Method - 1 (Using recursion) passing 33/94 cases (giving segmenatation fault error) -> but solution is correct
# # use var1 = root, var2 = root instead of using deepcopy
import copy, sys
sys.setrecursionlimit(1000000)

class Solution:
    def printBoundaryView(self, root):
        # Code here
        res = [root.data]
        
        if not root.left and not root.right:
            return res
        
        var1 = root # dont use copy.deepcopy(root)
        var2 = root # dont use copy.deepcopy(root)
        
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


# # Method - 2 (without using recursion) passing 33/94 cases (giving segmenatation fault error) -> but solution is correct
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
import copy

class Solution:
    def printBoundaryView(self, root):
        res = [root.data]
        
        if not root.left and not root.right:
            return res
        
        var1 = root # dont use copy.deepcopy(root)
        var2 = root # dont use copy.deepcopy(root)
        
        if var1.left:
            var1 = var1.left
            while var1:
                if not var1.left and not var1.right:
                    break
                
                res.append(var1.data)
                if var1.left:
                    var1 = var1.left
                else:
                    var1 = var1.right
        
        def bottom_tree(root):
            st = []
            res = []
            curr = root
            while st or curr:
                while curr:
                    st.append(curr)
                    curr = curr.left
                
                curr = st.pop()
                if not curr.left and not curr.right:
                    res.append(curr.data)
                curr = curr.right
    
            return res
        
        res.extend(bottom_tree(var2))
        
        right = []
        if root.right:
            right_node = root.right
            while right_node:
                if not right_node.right and not right_node.left:
                    break
                
                right.append(right_node.data)
                if right_node.right:
                    right_node = right_node.right
                else:
                    right_node = right_node.left

        res.extend(right[::-1])
        return res