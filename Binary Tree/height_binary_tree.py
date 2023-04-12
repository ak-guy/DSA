class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        def sol(root):
            if not root:
                return 0
            
            return 1 + max(sol(root.left), sol(root.right))
        
        return sol(root)
    
# see driver code from gfg