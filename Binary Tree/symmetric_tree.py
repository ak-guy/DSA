class Solution:
    # return true/false denoting whether the tree is Symmetric or not
    def isSymmetric(self, root):
        def sol(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
                
            if root1.data != root2.data:
                return False
                
            left = sol(root1.left, root2.right)
            right = sol(root1.right, root2.left)
            
            return left and right

        return sol(root, root)